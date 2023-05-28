import pygame
import math
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
X_POSITION, Y_POSITION = 400, 530
jumping = False

Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/char_stand.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/char_jump.png"), (48, 64))
mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

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

obstacle_group = pygame.sprite.Group()

run = True
while run:

    clock.tick(FPS)

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll,0))
        bg_rect.x = i * bg_width + scroll

    # Generate random obstacles
    if random.randint(0, 100) < 5:
        new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 100)
        obstacle_group.add(new_obstacle)

    # Move obstacles
    for obstacle in obstacle_group:
        obstacle.rect.x -= 5

    # Draw obstacles
    obstacle_group.draw(screen)

    # Handle character jumping
    if jumping:
        mario_rect.y -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if mario_rect.bottom >= Y_POSITION:
            mario_rect.bottom = Y_POSITION
            jumping = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        Y_VELOCITY = JUMP_HEIGHT

    # Draw character
    if jumping:
        screen.blit(JUMPING_SURFACE, mario_rect)
    else:
        screen.blit(STANDING_SURFACE, mario_rect)

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
