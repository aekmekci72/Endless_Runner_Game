import pygame
import math
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

bg = pygame.image.load("images/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
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
        freq-=5

    for obstacle in obstacle_group:
        obstacle.rect.x -= 5

    obstacle_group.draw(screen)
    player.draw(screen)

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up arrow")
        if event.type==pygame.MOUSEBUTTONDOWN:
            position=pygame.mouse.get_pos()
            print("mouse clicked")
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
