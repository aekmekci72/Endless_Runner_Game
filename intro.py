import pygame
import os
import subprocess

pygame.init()

screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Mini-Game Hub")

font = pygame.font.Font(None, 36)

games = [
    {"name": "Endless Runner", "path": "endless_runner.py"},
    {"name": "Tic Tac Toe", "path": "tic_tac_toe.py"},
    {"name": "Space Invaders", "path": "space_invaders.py"},
    {"name": "Pong", "path": "pong.py"},
]

button_width = 200
button_height = 50
button_padding = 20
button_start_y = (screen_height - (len(games) * (button_height + button_padding))) // 2

background_color = (0, 0, 0)
button_color = (255, 255, 255)
text_color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for game in games:
                    button_rect = pygame.Rect(
                        (screen_width - button_width) // 2,
                        button_start_y + games.index(game) * (button_height + button_padding),
                        button_width,
                        button_height
                    )
                    if button_rect.collidepoint(mouse_pos):
                        print('clicked')
                        game_path = game['path']
                        subprocess.Popen(["python", game_path])
                        running = False

    screen.fill(background_color)

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

    pygame.display.flip()

pygame.quit()
