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
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        r=random.randint(1,len(obslist))-1
        self.image = pygame.transform.scale((obslist[r])[0], ((obslist[r])[1], (obslist[r])[2]))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.standing_surface = pygame.transform.scale(pygame.image.load("images/char_stand.png"), (48, 64))
        self.jumping_surface = pygame.transform.scale(pygame.image.load("images/char_jump.png"), (48, 64))
        self.image = self.standing_surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.is_jumping = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.y >= SCREEN_HEIGHT - 65:
            self.rect.y = SCREEN_HEIGHT - 65
            self.velocity_y = 0
            self.is_jumping = False

        die = pygame.sprite.spritecollide(self, obstacle_group, False)
        if die:
            run = False

        if self.is_jumping:
            self.image = self.jumping_surface
        else:
            self.image = self.standing_surface
obstacle_group = pygame.sprite.Group()
run = True
freq=250
counter=0

player = Player(50, SCREEN_HEIGHT - 65)
player_group = pygame.sprite.Group()
player_group.add(player)
while run:
    
    clock.tick(FPS)
    
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll,0))
        bg_rect.x = i * bg_width + scroll
    counter+=1
    if counter==freq:
        new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 50)
        obstacle_group.add(new_obstacle)
        counter=0
        freq-=5
        freq-=10

    for obstacle in obstacle_group:
        obstacle.rect.x -= 5
    obstacle_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    scroll -= 5
    die = pygame.sprite.spritecollide(player, obstacle_group, False)
    if die:
        run = False
    if abs(scroll) > bg_width:
        scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not player.is_jumping: 
                player.velocity_y = JUMP_FORCE
                player.is_jumping = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print("mouse clicked")
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()