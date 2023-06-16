#FOR ALL GAMES, PAUSE AND QUIT, LEADERBOARD, HIGH SCORE

import random
import pygame
import os
import subprocess

pygame.init()

screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Mini-Game Hub")

font = pygame.font.Font(None, 36)


width = screen.get_width()
height = screen.get_height()
splash_page = pygame.image.load('images/games.png')
scaled_splash = pygame.transform.scale(splash_page, (800, 800))

class Ball:
    def __init__(self):
        self.radius = 20
        self.color = (255, 0, 0)  
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = -self.radius
        self.velocity = 0
        self.gravity = 0.5

    def update(self):
        self.y += self.velocity
        self.velocity += self.gravity

        if self.y + self.radius >= screen_height:
            self.y = screen_height - self.radius
            self.velocity *= -0.8

            if abs(self.velocity) < 5:
                self.y=screen_height-15

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)

balls=[]

running = True

clock = pygame.time.Clock()

freq=200


while running:
    r=random.randint(0,freq)
    if r<5:
        ball=Ball()
        balls.append(ball)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            freq+=1
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0]>490 and mouse_pos[0]<850 and mouse_pos[1]>305 and mouse_pos[1]<400:
                    subprocess.Popen("python endless_runner.py")
                    pygame.quit()
                if mouse_pos[0]>490 and mouse_pos[0]<850 and mouse_pos[1]>450 and mouse_pos[1]<545:
                    subprocess.Popen("python tic_tac_toe.py")
                    pygame.quit()
                if mouse_pos[0]>490 and mouse_pos[0]<850 and mouse_pos[1]>610 and mouse_pos[1]<700:
                    subprocess.Popen("python space_invaders.py") 
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1260 and mouse_pos[1]>135 and mouse_pos[1]<230:
                    subprocess.Popen("python pong.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1260 and mouse_pos[1]>265 and mouse_pos[1]<350:
                    subprocess.Popen("python flappy_bird.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1260 and mouse_pos[1]>380 and mouse_pos[1]<470:
                    subprocess.Popen("python clicker.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1260 and mouse_pos[1]>495 and mouse_pos[1]<585:
                    subprocess.Popen("python snakeworking.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1260 and mouse_pos[1]>610 and mouse_pos[1]<700:
                    subprocess.Popen("python race.py")
                    pygame.quit()
                
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running=False

    
    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))

    screen.blit(scaled_splash, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
