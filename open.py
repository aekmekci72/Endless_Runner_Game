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
    y = random.randrange(0,height)
    speed = random.randrange(10, 15)
    direction = random.choice([-1, 1]) 
    loop_height = random.randint(50, 150)  
    leafFall.append([x, y, speed, direction, loop_height, False])


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


counter = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            subprocess.Popen("python intro.py")

    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))

    screen.blit(scaled_splash, (0, 0))

    for i in range(len(leafFall)-1,0,-1):
        leaf = pygame.transform.scale(pygame.image.load("images/leaf.png"), (50, 50))
        screen.blit(leaf, (leafFall[i][0], leafFall[i][1]))

        leafFall[i][1] += leafFall[i][2]  

        if not leafFall[i][5]:  
            if leafFall[i][1] > leafFall[i][4]:
                leafFall[i][0] += leafFall[i][3]  
                leafFall[i][5] = True 
        else:  
            leafFall[i][0] += leafFall[i][3] 

        if leafFall[i][1] > height:
            leafFall.remove(leafFall[i])
            x = random.randrange(0, width)
            y = 0
            speed = random.randrange(10, 15)
            direction = random.choice([-1, 1]) 
            loop_height = random.randint(50, 150)  
            leafFall.append([x, y, speed, direction, loop_height, False])
        elif leafFall[i][0] < 0 or leafFall[i][0] > width:
            leafFall[i][3] *= -1  

    pygame.display.update()
    clock.tick(60)

pygame.quit()
