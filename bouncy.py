import pygame
import random

pygame.init()

screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Bouncy")

background_color = (255, 255, 255)


class Ball:
    def __init__(self):
        self.radius = 20
        self.color = (255, 0, 0)  # Red
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


balls = []
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ball = Ball()
            balls.append(ball)
            mouse_pos = pygame.mouse.get_pos()

    screen.fill(background_color)

    for ball in balls:
        ball.update()
        ball.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
