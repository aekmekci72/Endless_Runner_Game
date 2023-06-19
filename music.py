import pygame

music_initialized = False

def play_music():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  # -1 to loop the music indefinitely
        music_initialized = True
    else:
        pygame.mixer.music.unpause()
