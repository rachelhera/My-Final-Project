import pygame
from pygame.locals import *
from random import randint

#Global variables for the game
gameWidth = 1000                             #Game window gameWidth
gameHeight = 500                             #Game window gameHeight
FPS = 60
FPS = randint(60, 100)                       #Frames per second

birdHeight = 10                              #Height of the bird
birdWidth = 15                               #Width of the bird
jumpSteps = 15
jumpSteps = randint(9, 15)                   #Pixels to move
jumpPixels = 4                               #Pixels per frame
dropPixels = 3                               #Pixels per frame

groundHeight = 45                            #Height of the ground
pipeWidth = 52                               #Width of a pipe
pipeHeight = 320                             #Max Height of a pipe
#pipesSpace = 8 * birdHeight
pipesSpace = 200
pipesSpace = randint(150, 200)               #Space between pipes
pipesAddInterval = 2000
pipesAddInterval = randint(1000, 2000)       #Milliseconds

pixelsFrame = 2                              #Pixels per frame
getNewPipe = USEREVENT + randint(1, 5)       #Custom event

pygame.init()                                #Initialize pygame
screenResolution = pygame.display.Info()     #Get screen resolution
pygame.quit()                                #Close pygame

gameScore = 0                                #Game gameScore
waitClick = True