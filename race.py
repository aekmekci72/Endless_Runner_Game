# add a restart feature, maybe add a feature where other cars can merge lanes (with an indicator to make game harder), better position you died message

import random; import pygame as py; from pygame.locals import *

clock = py.time.Clock()

sh = 700
sw = 550
run = False

path = (100, 0, 300, sh) #road

win = (sw, sh)

py.init()
py.display.set_caption('Zoom Zoom')
display = py.display.set_mode(win)

othercars = [py.image.load(f'images/{f}') for f in ['car2.png', 'car3.png', 'car4.png', 'car5.png']]
death = py.image.load('images/dead.png')


scroll_lane = 0 #scrolling bg
sprite_init = py.sprite.Sprite

class Setup(sprite_init):
    def __init__(self, image, x, y):
        self.image = py.transform.smoothscale(image, (70, 70))
        self.rect = self.image.get_rect(center=(x, y))
        super().__init__()
    
score = 0
starty = 650
startx = 250 

class PlayerVehicle(Setup):
    def __init__(self, x, y):
        pic = py.image.load('images/car1.png')
        super().__init__(pic, x, y)
      

player = PlayerVehicle(startx, starty)
players = py.sprite.Group()
players.add(player)

lane_coordinates = [150, 250, 350]

dividerh = 40 #white lines of lane
dividerw = 9 #white lines of lane

edge_r = (395, 0, dividerh, sh) #right edge
edge_l = (95, 0, dividerw, sh) #left edge

speed=2.1

running = True
enemy = py.sprite.Group()

showdeath = death.get_rect()

while running==True:
    
    display.fill(("#99EDC3")) #grass
        
    #edges
    py.draw.rect(display, ("#74B72E"), edge_r)
    py.draw.rect(display, ("#74B72E"), edge_l)

    py.draw.rect(display, (100, 100, 100), path) #road

    clock.tick(120)
    
    for i in py.event.get():            
        if i.type == KEYDOWN:
            
            if i.key == K_RIGHT:
                if player.rect.center[0] < lane_coordinates[2]:
                    player.rect.x += 100

            if i.key == K_LEFT:
                if player.rect.center[0] > lane_coordinates[0]:
                    player.rect.x -= 100
                
            for car in enemy: # collision after lane switch
                if py.sprite.collide_rect(player, car):
                    
                    run = True
                    
                    if i.key == K_RIGHT:
                        player.rect.right = car.rect.left
                        showdeath.center = [
                            player.rect.right,
                            (player.rect.center[1] + car.rect.center[1]) / 2
                        ]
                    
                    if i.key == K_LEFT:
                        player.rect.left = car.rect.right
                        showdeath.center = [
                            player.rect.left,
                            (player.rect.center[1] + car.rect.center[1]) / 2
                        ]
                    
        if i.type == QUIT:
            running = False
         

    if scroll_lane >= dividerh * 2:
        scroll_lane = 0

    for y in range(-dividerh*2, sh, dividerh*2):
        for x in (lane_coordinates[0]+45, lane_coordinates[1]+45):
            py.draw.rect(display, (255,255,255), (x, y+scroll_lane, dividerw, dividerh))

    scroll_lane = scroll_lane+speed * 2  
    
    f1 = py.font.Font("images/Neucha-Regular.ttf", 24)
    show = f1.render('Score: ' + str(score), True, (255, 255, 255))

    
    if len(enemy) < 3:
        
        new = True #enough gap between vehicles
        for z in enemy:
            if z.rect.top < z.rect.height * 1.5:
                new = False
                
        if new==True:
            pic = random.choice(othercars)
            l = random.choice(lane_coordinates)
            car = Setup(pic, l, sh / -2)
            enemy.add(car)
        
    players.draw(display)
    enemy.draw(display)


    for t in enemy:
        t.rect.y = t.rect.y+speed
        
        if t.rect.top >= sh:
            t.kill()

            score += 1

            if score % 8 == 0:
                speed += 0.5
    
    div = show.get_rect()
    div.center = (44, 100)
    
    if py.sprite.spritecollide(player, enemy, True):
        run = True
        showdeath.center = [player.rect.centerx, player.rect.top]
            
    if run:
        display.blit(death, showdeath)
        
        py.draw.rect(display, ("#ED2939"), (0, 50, sw, 100))
        
        t1 = f1.render('Game over!', True, ("white"))
        div2 = t1.get_rect()
        div2.center = (sw / 2, 100)
        display.blit(t1, div2)
    
    display.blit(show, div)
            
    py.display.update()

py.quit()