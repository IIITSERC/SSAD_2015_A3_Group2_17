import pygame,sys
from pygame.locals import*
import main
from board import *
pygame.init()
displaysurf.fill(white)
all_items.draw(displaysurf)
main.game()
