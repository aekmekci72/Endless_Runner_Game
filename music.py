import pygame

music_initialized = False

def play_music():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music.wav")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  #
        music_initialized = True
    else:
        pygame.mixer.music.unpause()

def play_music2():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music2.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  
        music_initialized = True
    else:
        pygame.mixer.music.unpause()

def play_music3():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music3.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  
        music_initialized = True
    else:
        pygame.mixer.music.unpause()


def play_music4():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music4.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  
        music_initialized = True
    else:
        pygame.mixer.music.unpause()


def play_music5():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music5.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  
        music_initialized = True
    else:
        pygame.mixer.music.unpause()


def play_music6():
    global music_initialized

    if not music_initialized:
        pygame.mixer.init()
        pygame.mixer.music.load("images/music6.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)  
        music_initialized = True
    else:
        pygame.mixer.music.unpause()