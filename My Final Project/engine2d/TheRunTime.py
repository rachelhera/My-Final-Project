# Importing libraries
import os, sys, pygame, random, math
from pygame.locals import *
from TheFunctions import *
from TheClass import *
import TheVariables as gameVariables


def main():
    # Initializing pygame & mixer
    screen = initialize_pygame()
    #pimg = [pygame.image.load('../textures/birdvariant/' + str(i) +'.png') for i in range(1, 5)]
    # Setting up some timers
    clock = pygame.time.Clock()
    pygame.time.set_timer(getNewPipe, pipesAddInterval)

    # Loading the images | Creating the bird | Creating the ground | Creating the game list
    gamePipes = []
    gameBird = Bird()
    gameImagesbird = load_images_bird()
    gameImagesenv = load_images_env()
    gameImagesenvground = load_images_env_ground()
    gameImagesenvobs = load_images_env_obst()
    gameVariables.gameScore = 0
    gameGround = Ground(gameImagesenvground['ground'])

    # Loading the sounds
    jump_sound = pygame.mixer.Sound('assets/sounds/jump.ogg')
    score_sound = pygame.mixer.Sound('assets/sounds/score.ogg')
    dead_sound = pygame.mixer.Sound('assets/sounds/dead.ogg')
    ostbgm1 = pygame.mixer.Sound('assets/sounds/bgm1.ogg')
    ostbgm1.play()

    while (gameVariables.waitClick == True):
        # Draw everything and waitClick for the user to click to start the game
        # When we click somewhere, the bird will jump and the game will start
        screen.blit(gameImagesenv['background'], (0, 0))
        draw_text(screen, "Flappybird", 60, 50)
        draw_text(screen, "made by Undefined", 150, 15)
        draw_text(screen, "Click or mash the space to start", 385, 15)
        screen.blit(gameImagesenvground['ground'], (0, gameHeight - groundHeight))

        # Drawing a "floating" flappy bird
        gameBird.redraw(screen, gameImagesbird['bird'], gameImagesbird['bird2'], gameImagesbird['bird3'], gameImagesbird['bird4'])

        # Updating the screen
        pygame.display.update()

        # Checking if the user pressed left click or space and start (or not) the game
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN or (e.type == pygame.KEYDOWN and e.key == K_SPACE):
                gameBird.steps_to_jump = 15
                gameVariables.waitClick = False
    jump_sound.play()
    # Loop until...we die!
    while True:
        # Drawing the background
        screen.blit(gameImagesenv['background'], (0, 0))

        # Getting the mouse, keyboard or user events and act accordingly
        for e in pygame.event.get():
            if e.type == getNewPipe:
                p = PipePair(gameWidth, False)
                gamePipes.append(p)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                gameBird.steps_to_jump = jumpSteps
                jump_sound.play()
            elif e.type == pygame.KEYDOWN:
                if e.key == K_SPACE:
                    gameBird.steps_to_jump = jumpSteps
                    jump_sound.play()
                elif e.key == K_ESCAPE:
                    exit()

        # Tick! (new frame)
        clock.tick(FPS)

        # Updating the position of the gamePipes and redrawing them; if a pipe is not visible anymore,
        # we remove it from the list
        for p in gamePipes:
            p.x -= pixelsFrame
            if p.x <= - pipeWidth:
                gamePipes.remove(p)
            else:
                screen.blit(gameImagesenvobs['pipe-up'], (p.x, p.toph))
                screen.blit(gameImagesenvobs['pipe-down'], (p.x, p.bottomh))

        # Redrawing the ground
        gameGround.move_and_redraw(screen)

        # Updating the bird position and redrawing it
        gameBird.update_position()
        gameBird.redraw(screen, gameImagesbird['bird'], gameImagesbird['bird2'], gameImagesbird['bird3'], gameImagesbird['bird4'])

        # Checks for any collisions between the gamePipes, bird and/or the lower and the
        # upper part of the screen
        if any(p.check_collision((gameBird.bird_x, gameBird.bird_y)) for p in gamePipes) or \
                gameBird.bird_y < 0 or \
                gameBird.bird_y + birdHeight > gameHeight - groundHeight:
            dead_sound.play()
            ostbgm1.stop()
            break

        # There were no collision if we ended up here, so we are checking to see if
        # the bird went through one half of the pipe's gameWidth; if so, we update the gameScore
        for p in gamePipes:
            if (gameBird.bird_x > p.x and not p.score_counted):
                p.score_counted = True
                gameVariables.gameScore += 1
                score_sound.play()

        # Draws the gameScore on the screen
        draw_text(screen, gameVariables.gameScore, 50, 35)
        draw_text(screen, "Flappybird ", 30, 15)
        gameScore=gameVariables.gameScore
        # Updates the screen
        pygame.display.update()

    # We are dead now, so we make the bird "fall"
    while (gameBird.bird_y + birdHeight < gameHeight - groundHeight):
        # Redraws the background
        screen.blit(gameImagesenv['background'], (0, 0))

        # Redrawing the gamePipes in the same place as when it died
        for p in gamePipes:
            screen.blit(gameImagesenvobs['pipe-up'], (p.x, p.toph))
            screen.blit(gameImagesenvobs['pipe-down'], (p.x, p.bottomh))

        # Draws the ground piece to get the rolling effect
        gameGround.move_and_redraw(screen)

        # Makes the bird fall down and rotates it
        gameBird.redraw_dead(screen, gameImagesbird['bird'])

        # Tick!
        clock.tick(FPS * 3)

        # Updates the entire screen
        pygame.display.update()

    # Let's end the game!
    if not end_the_game(screen, gameScore):
        main()
    else:
        print('--------------------------[See ya soon again]-------------------------------')
        print('q7e2d has been shut off gracefully')
        #draw_text(screen, "Thank you for playing", 20, 15)
        #time.sleep(4)
        pygame.display.quit()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    # - If this module had been imported, __name__ would be 'Flappy Bird';
    # otherwise, if it was executed (by double-clicking the file) we would call main

    main()