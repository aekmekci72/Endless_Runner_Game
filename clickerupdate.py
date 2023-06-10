import pygame as py
import sys

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
        self.autoClickerBtn = py.Rect(10, 150, 185, 75)
        self.auto_clicker_on = False
        self.auto_clicker_cost = 50
        self.auto_clicker_timer = 0
        self.auto_clicker_cps = 1

        self.font = py.font.Font("images/Neucha-Regular.ttf", 25)

    def run(self):
        self.click()
        self.counter()
        self.upgrade()
        self.auto_clicker()

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
                self.cpc += 1

        if self.circle.collidepoint(self.pos):
            if py.mouse.get_pressed()[0]:
                self.isClicked=True
            else:
                if self.isClicked:
                    self.num_of_cookies +=self.cpc
                    self.isClicked=False
                else:
                    pass

        if self.autoClickerBtn.collidepoint(self.pos):
            if py.mouse.get_pressed()[0]:
                self.buy_auto_clicker()

    def upgrade(self):
        py.draw.rect(window, "#522920", self.upgradeBtn, border_radius=15)
        self.display_cost = font.render(f"Cost: {str(self.upgrade1_cost)}", True, "#eee0b1")
        self.upgrade1_description = self.font.render(f"+{self.cpc} cookie per click", True, "#eee0b1") 

        window.blit(self.upgrade1_description, (25, 65)) 
        window.blit(self.display_cost, (45, 85))

    def auto_clicker(self):
        if not self.auto_clicker_on:
            py.draw.rect(window, "#522920", self.autoClickerBtn, border_radius=15)
            self.auto_clicker_description = self.font.render(f"Buy Autoclicker ({self.auto_clicker_cost} cookies)", True, "#eee0b1")
            window.blit(self.auto_clicker_description, (25, 165))
        else:
            self.auto_clicker_timer += 1
            if self.auto_clicker_timer % 60 == 0:
                self.num_of_cookies += self.auto_clicker_cps
            py.draw.rect(window, "#16213e", self.autoClickerBtn, border_radius=15)
            self.auto_clicker_description = self.font.render(f"Autoclicker: {self.auto_clicker_cps} cps", True, "#eee0b1")
            window.blit(self.auto_clicker_description, (25, 165))

    def buy_auto_clicker(self):
        if self.num_of_cookies >= self.auto_clicker_cost:
            self.num_of_cookies -= self.auto_clicker_cost
            self.auto_clicker_on = True
            self.auto_clicker_cps=1


h = 600 
w = 800

py.display.set_caption("Cookie Clicker") 
window = py.display.set_mode(size=(w, h))

font2 = py.font.Font("images/Neucha-Regular.ttf", 50) 
font = py.font.Font("images/Neucha-Regular.ttf", 30)

background = py.image.load("images/background.png").convert()

game = Control()

heading = font2.render("Cookie Clicker", True, "white")

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
