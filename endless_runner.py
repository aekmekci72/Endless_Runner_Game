#make score work
#score=timer?
#power ups
#more obstacles


import pygame
import math
import random
import os
import subprocess


pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600
GRAVITY = 0.6
JUMP_FORCE = -15
DASH_MAX = 100
DASH_REGEN_RATE = 0.2
DASH_CONSUME_RATE = 1
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Runner Game")
bg = pygame.image.load("images/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()
score = 0


spike1 = [pygame.image.load("images/spike1.png").convert_alpha(), 50,50]
spike3 = [pygame.image.load("images/spike3.png").convert_alpha(), 150, 50]

obslist=[spike1,spike3]

scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1
indexon=0
megacount=0
jumpon=0
jumpcount=0
r=False

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
        # self.standing_surface = pygame.transform.scale(pygame.image.load("images/char_stand.png"), (48, 64))
        # self.jumping_surface = pygame.transform.scale(pygame.image.load("images/char_jump.png"), (48, 64))

        
        self.a1 = pygame.transform.scale(pygame.image.load("images/a1.png"), (48, 64))
        self.a2 = pygame.transform.scale(pygame.image.load("images/a2.png"), (48, 64))
        self.a3 = pygame.transform.scale(pygame.image.load("images/a3.png"), (48, 64))
        self.a4 = pygame.transform.scale(pygame.image.load("images/a4.png"), (48, 64))
        self.a5 = pygame.transform.scale(pygame.image.load("images/a5.png"), (48, 64))
        self.a6 = pygame.transform.scale(pygame.image.load("images/a6.png"), (48, 64))
        self.a7 = pygame.transform.scale(pygame.image.load("images/a7.png"), (48, 64))
        self.a8 = pygame.transform.scale(pygame.image.load("images/a8.png"), (48, 64))
        self.animlist=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8]

        self.j1 = pygame.transform.scale(pygame.image.load("images/j1.png"), (48, 64))
        self.j2 = pygame.transform.scale(pygame.image.load("images/j2.png"), (36, 48))
        self.j3 = pygame.transform.scale(pygame.image.load("images/j3.png"), (48, 64))
        self.jumplist=[self.j1,self.j2,self.j3]



        self.image = self.animlist[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = 0
        self.is_jumping = False
        self.dash = DASH_MAX

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.y >= SCREEN_HEIGHT - 65:
            self.rect.y = SCREEN_HEIGHT - 65
            self.velocity_y = 0
            self.is_jumping = False
            jumpcount=0
        self.dash+=DASH_REGEN_RATE
        if self.dash > DASH_MAX:
            self.dash = DASH_MAX
            

        die = pygame.sprite.spritecollide(self, obstacle_group, False)
        if die:
            run = False
        if self.is_jumping:
            self.image = self.jumplist[jumpon]
        else:
            self.image = self.animlist[indexon]
obstacle_group = pygame.sprite.Group()
global run
run = True
freq=250
counter=0
global pause
pause=False

scrollmin=5

player = Player(50, SCREEN_HEIGHT - 65)
player_group = pygame.sprite.Group()
player_group.add(player)

def paused():
    global pause, run
    while pause==True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause=False
                if event.key == pygame.K_q:
                    run=False
                    pause=False
                    
                        
        pygame.display.update()
        clock.tick(15)  
dash_bar_width = player.dash / DASH_MAX * 100
while run:
    if pause!=True:
        if player.is_jumping:
            jumpcount+=1
            if jumpcount<=7:
                jumpon=0
            elif jumpcount<=30:
                jumpon=1
            else:
                jumpon=2
        megacount+=1
        if(megacount%5==0):
            indexon+=1
            score+=1
            if indexon==8:
                indexon=0
        
        clock.tick(FPS)
        
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll,0))
            bg_rect.x = i * bg_width + scroll
        counter+=1
        if counter>=freq:
            new_obstacle = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT - 50)
            obstacle_group.add(new_obstacle)
            counter=0
            
    
        last_obstacle_passed = None
        for obstacle in obstacle_group:
            obstacle.rect.x -= scrollmin
            if player.rect.colliderect(obstacle.rect) and obstacle.rect.right < player.rect.left:
                last_obstacle_passed = obstacle  # Update last_obstacle_passed

        obstacle_group.draw(screen)
        player_group.update()
        player_group.draw(screen)
        scroll -= scrollmin


        die = pygame.sprite.spritecollide(player, obstacle_group, False)
        if die:
            run = False
        if abs(scroll) > bg_width:
            scroll = 0

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not player.is_jumping: 
                    player.velocity_y = JUMP_FORCE
                    player.is_jumping = True
                    jumpcount=0
                if event.key == pygame.K_p:
                    pause=True
                    paused()
                if event.key == pygame.K_q:
                    run=False
                if event.key == pygame.K_RIGHT:
                    r=True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    r=False
                    scrollmin=5
                    freq=250
            

            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                print("mouse clicked")

        if r==True:
            if player.dash >=DASH_CONSUME_RATE:
                player.dash-=DASH_CONSUME_RATE
                dash_bar_width = player.dash / DASH_MAX * 100
                scrollmin=10
                freq=125
            else:
                scrollmin=5
                freq=250

        dash_bar_width = player.dash / DASH_MAX * 100
        pygame.draw.rect(screen, (255,255,255), (10,50, 100,10))
        pygame.draw.rect(screen,(0,255,0),(10,50,(dash_bar_width),10))
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))


        pygame.display.update()
subprocess.Popen("python end_screen.py")
pygame.quit()