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

games = [
    {"name": "Endless Runner", "path": "endless_runner.py"},
    {"name": "Tic Tac Toe", "path": "tic_tac_toe.py"},
    {"name": "Space Invaders", "path": "space_invaders.py"},
    {"name": "Pong", "path": "pong.py"},
    {"name": "Flappy Bird", "path": "flappy_bird.py"},
    {"name": "Clicker Simulator", "path": "clicker.py"},
    {"name": "Snake", "path": "snakeworking.py"},
    {"name": "Car Race", "path": "race.py"},
    
]

button_width = 200
button_height = 50
button_padding = 20
button_start_y = (screen_height - (len(games) * (button_height + button_padding))) // 2

background_color = (225,225,225)
button_color = (0, 0, 0)
text_color = (225,225, 225)


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
                print(mouse_pos)
                print(mouse_pos)
                if mouse_pos[0]>475 and mouse_pos[0]<860 and mouse_pos[1]>310 and mouse_pos[1]<415:
                    subprocess.Popen("python endless_runner.py")
                    pygame.quit()
                if mouse_pos[0]>475 and mouse_pos[0]<860 and mouse_pos[1]>475 and mouse_pos[1]<575:
                    subprocess.Popen("python tic_tac_toe.py")
                    pygame.quit()
                if mouse_pos[0]>475 and mouse_pos[0]<860 and mouse_pos[1]>645 and mouse_pos[1]<745:
                    subprocess.Popen("python space_invaders.py") 
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1280 and mouse_pos[1]>125 and mouse_pos[1]<225:
                    subprocess.Popen("python pong.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1280 and mouse_pos[1]>260 and mouse_pos[1]<360:
                    subprocess.Popen("python flappy_bird.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1280 and mouse_pos[1]>390 and mouse_pos[1]<490:
                    subprocess.Popen("python clicker.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1280 and mouse_pos[1]>520 and mouse_pos[1]<620:
                    subprocess.Popen("python snakeworking.py")
                    pygame.quit()
                if mouse_pos[0]>900 and mouse_pos[0]<1280 and mouse_pos[1]>650 and mouse_pos[1]<750:
                    subprocess.Popen("python race.py")
                    pygame.quit()
                
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running=False

    screen.fill(background_color)

    for ball in balls:
        ball.update()
        ball.draw()

    for game in games:
        button_rect = pygame.Rect(
            (screen_width - button_width) // 2,
            button_start_y + games.index(game) * (button_height + button_padding),
            button_width,
            button_height
        )
        pygame.draw.rect(screen, button_color, button_rect)

        text_surface = font.render(game["name"], True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    scaled_splash = pygame.transform.smoothscale(scaled_splash, (width, height))

    screen.blit(scaled_splash, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
