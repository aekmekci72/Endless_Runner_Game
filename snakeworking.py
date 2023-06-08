#apple thing

import pygame as py, sys, random
py.init()
clock = py.time.Clock()
screen_width=800
screen_height =800
tile = 50
score_font = py.font.Font("images/Neucha-Regular.ttf", tile*2)
window = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Snake Game")


class Food:
    def __init__(self):
        randheight=random.randint(tile, screen_height-tile)/tile
        self.y = int(randheight) * tile

        randwidth = random.randint(tile, screen_width-tile)/tile
        self.x = int(randwidth) * tile

        self.rect = py.Rect(self.x, self.y, tile, tile)

    def draw(self):
        py.draw.rect(window, "red", self.rect)


class Snake:
    def __init__(self):
        self.gameOver = False

        self.xdir = 1
        self.x=tile

        self.ydir = 0
        self.y = tile

        self.length = [
            py.Rect(self.x-tile, self.y, tile, tile)
        ]

        self.start = py.Rect(self.x, self.y, tile, tile)
    
    def move(self):
        global food

        self.length.append(self.start)
        l = len(self.length)-1
        for x in range(l):
            i = self.length[x+1]
            self.length[x].x=i.x
            self.length[x].y = i.y
        self.start.y += self.ydir * tile
        self.start.x += self.xdir * tile
        self.length.remove(self.start)

        
        if self.gameOver:
            self.x, self.y = tile, tile

            
            self.length = [py.Rect(self.x-tile, self.y, tile, tile)]
            self.start = py.Rect(self.x, self.y, tile, tile)

            self.ydir = 0
            self.xdir = 1
            
            self.gameOver = False
            food = Food()

        for i in self.length:
            if self.start.colliderect(i):
                self.gameOver = True
            if not window.get_rect().colliderect(self.start):
                self.gameOver = True




food = Food()
snake1 = Snake()

start_text = score_font.render("Press space to start", True, "white")
start_rect = start_text.get_rect(center=(screen_width/2, screen_height/2))

score = score_font.render("1", True, "white")
score_box = score.get_rect(center=(screen_width/2, screen_height/7))

# light_mask = py.Surface((screen_width, screen_height))
# light_mask.set_alpha(128)
# light_mask.fill((0, 0, 0))

while True:
    playing = False

    while not playing:
        # if snake1.gameOver:
        #     py.quit()
        #     sys.exit()

        for i in py.event.get():
            if i.type == py.QUIT:
                py.quit()
                sys.exit()
            
            if i.type == py.KEYDOWN:
                if i.key == py.K_SPACE:
                    playing = True

        window.fill('black')
        start_text = score_font.render("Press space to start", True, "white")
        start_rect = start_text.get_rect(center=(screen_width/2, screen_height/2))
        window.blit(start_text, start_rect)
        py.display.update()
        clock.tick(10)

    while playing:

        # if snake1.gameOver:
        #     py.quit()
        #     sys.exit()

        for i in py.event.get():
            if i.type == py.QUIT:
                py.quit()
                sys.exit()

            if i.type == py.KEYDOWN:
                if i.key == py.K_SPACE:
                    playing = False

        window.fill('black')

        food.draw()
        snake1.move()
        
        showscore = score_font.render(f"{len(snake1.length)}", True, "white")
        py.draw.rect(window, "green", snake1.start)
        for unit in snake1.length:
            py.draw.rect(window, "green", unit)
        window.blit(showscore, score_box)

        if snake1.start.colliderect(food.rect):
            snake1.length.append(py.Rect(unit.x, unit.y, tile, tile))
            food = Food()

        py.display.update()
        clock.tick(10)

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_DOWN and snake1.ydir != -1:
                        snake1.ydir = 1
                        snake1.xdir = 0
                    elif event.key == py.K_UP and snake1.ydir != 1:
                        snake1.ydir = -1
                        snake1.xdir = 0
                    elif event.key == py.K_RIGHT and snake1.xdir != -1:
                        snake1.ydir = 0
                        snake1.xdir = 1
                    elif event.key == py.K_LEFT and snake1.xdir != 1:
                        snake1.ydir = 0
                        snake1.xdir = -1

                    if event.key == py.K_s and snake1.ydir != -1:
                        snake1.ydir = 1
                        snake1.xdir = 0
                    elif event.key == py.K_w and snake1.ydir != 1:
                        snake1.ydir = -1
                        snake1.xdir = 0
                    elif event.key == py.K_d and snake1.xdir != -1:
                        snake1.ydir = 0
                        snake1.xdir = 1
                    elif event.key == py.K_a and snake1.xdir != 1:
                        snake1.ydir = 0
                        snake1.xdir = -1

            snake1.move()
            food.draw()
            
            window.fill('black')

            score = score_font.render(f"{len(snake1.length)-1}", True, "white")

            py.draw.rect(window, "green", snake1.start)
            for square in snake1.length:
                py.draw.rect(window, "green", square)
            window.blit(score, score_box)

            if snake1.start.colliderect(food.rect):
                snake1.length.append(py.Rect(square.x, square.y, tile, tile))
                food = Food()

            
            py.display.update()
            clock.tick(10)