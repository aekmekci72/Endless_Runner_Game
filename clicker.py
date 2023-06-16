#click multiplier
#click assistant 
#time warp

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
        self.upgradeBtn =  py.Rect(710, 50, 185, 75)
        self.autoClickerBtn = py.Rect(710, 150, 185, 125)
        self.clickMultBtn = py.Rect(710, 300, 185, 125)
        self.auto_clicker_on = False
        self.auto_clicker_cost = 150
        self.auto_clicker_timer = 0
        self.auto_clicker_cps = 1

        self.click_multipliers=1
        self.click_multipliercost=1000

        self.num_autoclicker=0
        self.font = py.font.Font("images/Neucha-Regular.ttf", 25)

    def run(self):
        self.click()
        self.counter()
        self.upgrade()
        self.auto_clicker()
        self.click_multiplier()

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
                    self.num_of_cookies +=(self.cpc*self.click_multipliers)
                    self.isClicked=False
                else:
                    pass

        if self.autoClickerBtn.collidepoint(self.pos):
            if py.mouse.get_pressed()[0]:
                self.buy_auto_clicker()
        if self.clickMultBtn.collidepoint(self.pos):
            if py.mouse.get_pressed()[0]:
                self.buy_click_multiplier()

    def upgrade(self):
        py.draw.rect(window, "#522920", self.upgradeBtn, border_radius=15)
        self.display_cost = font.render(f"Cost: {str(self.upgrade1_cost)}", True, "#eee0b1")
        self.upgrade1_description = self.font.render(f"+{self.cpc} cookie per click", True, "#eee0b1") 

        window.blit(self.upgrade1_description, (725, 65)) 
        window.blit(self.display_cost, (745, 85))

    def auto_clicker(self):
        if not self.auto_clicker_on:
            py.draw.rect(window, "#522920", self.autoClickerBtn, border_radius=15)
            self.auto_clicker_description = self.font.render(f"Buy Autoclicker", True, "#eee0b1")
            self.auto_clicker_c = self.font.render(f"({self.auto_clicker_cost} cookies)", True, "#eee0b1")
            s=self.auto_clicker_cps+1+self.num_autoclicker
            self.auto_clicker_update = self.font.render(f"0 -> {s} cps)", True, "#eee0b1")
            window.blit(self.auto_clicker_description, (725, 165))
            window.blit(self.auto_clicker_c, (725, 195))
            window.blit(self.auto_clicker_update, (725, 225))
            
        else:
            self.auto_clicker_timer += 1
            if self.auto_clicker_timer % 60 == 0:
                self.num_of_cookies += self.auto_clicker_cps
            py.draw.rect(window, "#522920", self.autoClickerBtn, border_radius=15)
            self.auto_clicker_description = self.font.render(f"Buy Autoclicker", True, "#eee0b1")
            self.auto_clicker_c = self.font.render(f"({self.auto_clicker_cost} cookies)", True, "#eee0b1")
            s=self.auto_clicker_cps+1+self.num_autoclicker
            self.auto_clicker_update = self.font.render(f"{int(self.auto_clicker_cps)} -> {s} cps)", True, "#eee0b1")
            window.blit(self.auto_clicker_description, (725, 165))
            window.blit(self.auto_clicker_c, (725, 195))
            window.blit(self.auto_clicker_update, (725, 225))

    def buy_auto_clicker(self):
        if self.num_of_cookies >= self.auto_clicker_cost:
            self.num_of_cookies -= self.auto_clicker_cost
            self.auto_clicker_on = True
            self.auto_clicker_cps+=1+self.num_autoclicker
            self.auto_clicker_cost*=5
            self.num_autoclicker+=1

    def click_multiplier(self):
        py.draw.rect(window, "#522920", self.clickMultBtn, border_radius=15)
        self.clickmult_description = self.font.render(f"Buy Click Multiplier", True, "#eee0b1")
        self.clickmult_c = self.font.render(f"({self.click_multipliercost} cookies)", True, "#eee0b1")
        self.clickmult_update = self.font.render(f"{int(self.click_multipliers)}x -> {self.click_multipliers+0.25}x)", True, "#eee0b1")
        window.blit(self.clickmult_description, (725, 315))
        window.blit(self.clickmult_c, (725, 345))
        window.blit(self.clickmult_update, (725, 375))

    def buy_click_multiplier(self):
        if self.num_of_cookies >=self.click_multipliercost:
            self.num_of_cookies-=self.click_multipliercost
            self.click_multipliercost*=2
            self.click_multipliers +=0.25

background = py.image.load("images/background.png")

h = background.get_height()-50
w = background.get_width()*2

py.display.set_caption("Cookie Clicker") 
window = py.display.set_mode(size=(w, h))

font2 = py.font.Font("images/Neucha-Regular.ttf", 50) 
font = py.font.Font("images/Neucha-Regular.ttf", 30)


game = Control()

heading = font2.render("Cookie Clicker", True, "white")

while True: 
    window.blit(background, (0,0))
    window.blit(background, (w/2,0))

    for i in py.event.get():
        if i.type == py.QUIT:
            py.quit()
            sys.exit()

    

    window.blit(heading, (270, 50))

    game.run()
    py.display.update()
    clock.tick(60)
