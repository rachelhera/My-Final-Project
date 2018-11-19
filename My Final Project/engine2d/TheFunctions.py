import sys, os, random, pygame
from TheVariables import *
import time

def initialize_pygame():
    pygame.init()
    pygame.mixer.init()

    # Opening the window in the center of the screen
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
    (screenResolution.current_w - gameWidth) / 2, (screenResolution.current_h - gameHeight) / 2)
    screen = pygame.display.set_mode([gameWidth, gameHeight], pygame.DOUBLEBUF, 32)
    pygame.display.set_icon(pygame.image.load('assets/textures/icon.ico'))
    pygame.display.set_caption("Flappy Bird ")

    return screen


def load_images_bird():
    # - Loading all the images required for the game from the images folder
    # and returning a dictionary of them as following:

    def load_image(img_file_name):
        file_name = os.path.join('.', 'assets/textures', img_file_name)
        img2 = pygame.image.load(file_name)
        img2 = pygame.transform.scale(img2, (90, 85))
        img2.convert()
        return img2

    return {'bird': load_image('birdvariant/1.png'),
            'bird2': load_image('birdvariant/2.png'),
            'bird3': load_image('birdvariant/3.png'),
            'bird4': load_image('birdvariant/4.png')}

def load_images_env_obst():
    def load_image(img_file_name):

        file_name = os.path.join('.', 'assets/textures', img_file_name)
        img = pygame.image.load(file_name)
        #img = pygame.transform.scale(img, (80, 100))
        img.convert()
        return img

    return {'pipe-up': load_image('obstacle/pipe-up' + str(random.randint(1, 1)) + '.png'),
            'pipe-down': load_image('obstacle/pipe-down' + str(random.randint(1, 1)) + '.png')}
    #rescalehacks

def load_images_env():
    def load_image(img_file_name):

        file_name = os.path.join('.', 'assets/textures', img_file_name)
        img = pygame.image.load(file_name)
        img = pygame.transform.scale(img, (1000, 800))
        img.convert()
        return img

    return {'background': load_image('envbg/env' + str(random.randint(1, 6)) + '.png')}
    #rescalehacks

def load_images_env_ground():
    def load_image(img_file_name):

        file_name = os.path.join('.', 'assets/textures', img_file_name)
        img = pygame.image.load(file_name)
        img = pygame.transform.scale(img, (2000, 100))
        img.convert()
        return img

    return {'ground': load_image('envbg/ground.png')}
    #rescalehacks


def draw_text(screen, text, y_pos, size):
    # Drawing a black text (bigger) and then a white text, smaller
    # over it to get the desired gameScore effect
    font = pygame.font.Font("assets/data/04b_19.TTF", size)
    score_text_b = font.render(str(text), 1, (0, 0, 0))
    score_text_w = font.render(str(text), 1, (255, 255, 255))

    x_pos_b = (gameWidth - score_text_b.get_width()) / 2
    x_pos_w = (gameWidth - score_text_w.get_width()) / 2
    screen.blit(score_text_b, (x_pos_b + 2, y_pos - 1))
    screen.blit(score_text_w, (x_pos_w, y_pos))


def end_the_game(screen, gameScore):
    # Draws a rectangle & shows the gameScore & updates the highscore
    pygame.draw.rect(screen, (0, 0, 0), (375, gameHeight / 2 - 77, 254, 154))
    pygame.draw.rect(screen, (239, 228, 150), (377, gameHeight / 2 - 75, 250, 150))
    draw_text(screen, "Your Score: " + str(gameScore), 200, 35)
    f = open("assets/data/highscore.txt", "r+")
    hs = int(f.readline())
    if (gameScore > hs):
        hs = gameScore
        f.seek(0)
        f.truncate()
        f.write(str(gameScore))
    f.close()

    draw_text(screen, "Highscore: " + str(hs), 250, 35)
    draw_text(screen, "Press space to restart", 335, 20)
    draw_text(screen, "Press esc to exit", 355, 20)

    # Updates the entire screen for the last time
    pygame.display.update()

    # Gets the keyboard events to se if the user wants to restart the game
    while True:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    return 0
                elif e.key == K_ESCAPE:
                    draw_text(screen, "Thank you for playing", 20, 15)
                    time.sleep(4)
                    return 1