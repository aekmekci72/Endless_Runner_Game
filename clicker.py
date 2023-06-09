#autoclicker, boosts

import pygame as py, sys

py.init()
clock = py.time.Clock()

class Control:
    def __init__(self):
        self.cpc = 1
        self.num_of_cookies = 0
        self.upgrade1_cost = 5
        self.isClicked = False
        self.color = "#9D7E67"


        self.circle = py.Rect(400-150,300-150,300,300)
        self.upgradeBtn =  py.Rect(10, 50, 185, 75)


        self.font = py.font.Font("images/Neucha-Regular.ttf", 25)
    
    def run(self):
        self.click()
        self.counter()
        self.upgrade()

    def counter(self):
        x=str([self.num_of_cookies])
        self.cookiecount = font2.render("Cookies: "+x, True, "white")
        window.blit(self.cookiecount, (20,500))

    
    def click(self):
        self.pos = py.mouse.get_pos()
        py.draw.rect(window, self.color, self.circle, border_radius = 150)

        if self.upgradeBtn.collidepoint(self.pos):
            if py.mouse.get_pressed()[0] and self.num_of_cookies>=self.upgrade1_cost:
                self.num_of_cookies-=self.upgrade1_cost
                self.cpc += 1
                self.upgrade1_cost *= 2
                self.cpc+=1

        if self.circle.collidepoint(self.pos):
            if py.mouse.get_pressed()[0]:
                self.isClicked=True
            else:
                if self.isClicked:
                    self.num_of_cookies +=self.cpc
                    self.isClicked=False
                else:
                    pass

    def upgrade(self):
        py.draw.rect(window, "#522920", self.upgradeBtn, border_radius=15)
        self.display_cost = font.render(f"Cost: {str(self.upgrade1_cost)}", True, "#eee0b1")
        self.upgrade1_description = self.font.render(f"+{self.cpc} cookie per click", True, "#eee0b1")

        window.blit(self.upgrade1_description, (25, 65))           
        window.blit(self.display_cost, (45, 85))



h = 600
w = 800

# py.display.set_mode(size=(500,565))
py.display.set_caption("Cookie Clicker")
window = py.display.set_mode(size=(w, h))

font2 = py.font.Font("images/Neucha-Regular.ttf", 50)
font = py.font.Font("images/Neucha-Regular.ttf", 30)

background = py.image.load("images/background.png").convert()

game = Control()


heading =  font2.render("Cookie Clicker", True, "white")

while True:
    window.blit(background, (0,0))

    for i in py.event.get():
        if i.type == py.QUIT:
            py.quit()
            sys.exit()
            
        window.blit(heading, (270, 50))

        game.run()
        py.display.update()
        clock.tick(60)