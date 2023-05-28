import pygame
import math
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
GRAVITY = 0.6
JUMP_FORCE = -15


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

bg = pygame.image.load("images/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()


spike1 = [pygame.image.load("images/spike1.png").convert_alpha(), 50,50]
spike3 = [pygame.image.load("images/spike3.png").convert_alpha(), 150, 50]

obslist=[spike1,spike3]

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        r=random.randint(1,len(obslist))-1
        self.image = pygame.transform.scale((obslist[r])[0], ((obslist[r])[1], (obslist[r])[2]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface((25,25))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.is_jumping = False

obstacle_group = pygame.sprite.Group()

run = True
freq=250
counter=0

p = Player(50, SCREEN_HEIGHT - 75)
player=pygame.sprite.Group()
player.add(p)

while run:
    

    clock.tick(FPS)
    
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll,0))
        bg_rect.x = i * bg_width + scroll
    counter+=1
    if counter==freq:
        new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 100)
        obstacle_group.add(new_obstacle)
        counter=0
        freq-=10

    for obstacle in obstacle_group:
        obstacle.rect.x -= 5

    obstacle_group.draw(screen)
    player.draw(screen)

    p.velocity_y += GRAVITY
    
    p.rect.y += p.velocity_y
    
    if p.rect.y >= SCREEN_HEIGHT - 75:  
        p.rect.y = SCREEN_HEIGHT - 75
        p.velocity_y = 0
        p.is_jumping = False

    die = pygame.sprite.spritecollide(p, obstacle_group, False)
    if die:
        run = False

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not p.is_jumping: 
                p.velocity_y = JUMP_FORCE
                p.is_jumping = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print("mouse clicked")
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()
