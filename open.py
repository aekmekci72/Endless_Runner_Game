import pygame
import os
import subprocess
import random

pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption('Sick or Swim')

clock = pygame.time.Clock()
font = pygame.font.Font('images/Neucha-Regular.ttf', 60)
font1 = pygame.font.Font('images/PermanentMarker-Regular.ttf', 90)

color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Arial', 35)
text = smallfont.render('S T A R T', True, color)

splash_page = pygame.image.load('images/autumnarcade.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))

leafFall = []
for i in range(10):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    speed = random.randrange(10, 15)
    fall_margin = random.randint(-100, 100)
    orig = x
    leafFall.append([x, y, speed, fall_margin, orig])

counter = 1
print(leafFall)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            subprocess.Popen("python intro.py")

    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))

    screen.blit(scaled_splash, (0, 0))

    for i in range(len(leafFall) - 1, -1, -1):
        leaf = pygame.transform.scale(pygame.image.load("images/leaf.png"), (50, 50))
        screen.blit(leaf, (leafFall[i][0], leafFall[i][1]))
    
        leafFall[i][1] += leafFall[i][2]
        leafFall[i][0] += leafFall[i][3]/5
        leafFall[i][2]-=0.5
        if not (leafFall[i][0] > leafFall[i][4] + leafFall[i][3] and  leafFall[i][0] < leafFall[i][4] - leafFall[i][3] or leafFall[i][0] < leafFall[i][4] + leafFall[i][3] and  leafFall[i][0] > leafFall[i][4] - leafFall[i][3]):
            leafFall[i][3] *=-1
            leafFall[i][2]=random.randrange(10,15)

    if random.randint(0, 50) < 10:
        x = random.randrange(0, width)
        y = (0)
        speed = random.randrange(10, 15)
        fall_margin = random.randint(-100, 100)
        orig = x
        leafFall.append([x, y, speed, fall_margin, orig])

    pygame.display.update()
    clock.tick(250)

pygame.quit()
