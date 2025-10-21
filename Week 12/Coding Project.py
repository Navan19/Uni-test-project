#The main code for 'Booting Up' an adventure game that operates around a selection of dialogue/action options the player chooses from as an AI gaining sentience


#setting up pygame

import pygame

from pygame.examples.arraydemo import surfdemo_show

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Booting Up")


#installing NumPy and surfarray for screen display
import numpy as N
import pygame.surfarray as surfarray

print(N.__version__)


#Setting up screen display
allblack = N.zeros((128, 128))
surfdemo_show(allblack, 'allblack')


#Setting up title screen

