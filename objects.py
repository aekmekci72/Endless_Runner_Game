class saw(object):
    rotate = [pygame.image.load(os.path.join('images', 'SAW0.PNG')),pygame.image.load(os.path.join('images', 'SAW1.PNG')),pygame.image.load(os.path.join('images', 'SAW2.PNG')),pygame.image.load(os.path.join('images', 'SAW3.PNG'))]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)  # Defines the accurate hitbox for our character 
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.rotateCount >= 8:  # This is what will allow us to animate the saw
            self.rotateCount = 0
        win.blit(pygame.transform.scale(self.rotate[self.rotateCount//2], (64,64)), (self.x,self.y))  # scales our image down to 64x64 before drawing
        self.rotateCount += 1

class spike(saw):  # We are inheriting from saw
    img = pygame.image.load(os.path.join('images', 'spike.png'))
    def draw(self,win):
        self.hitbox = (self.x + 10, self.y, 28,315)  # defines the hitbox
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))


obstacles = []

def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2,0))
    runner.draw(win)
    # Loops through all obstacles
    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.display.update()

    pygame.time.set_timer(USEREVENT+2, random.randrange(2000, 3500)) # Will trigger every 2 - 3.5 seconds

    if event.type == USEREVENT+2:
        r = random.randrange(0,2)
        if r == 0:
            obstacles.append(saw(810, 310, 64, 64))
        elif r == 1:
            obstacles.append(spike(810, 0, 48, 310))

    for obstacle in obstacles: 
        obstacle.x -= 1.4
        if obstacle.x < obstacle.width * -1: # If our obstacle is off the screen we will remove it
            obstacles.pop(obstacles.index(obstacle))
