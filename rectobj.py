import pygame, sys
from pygame.locals import *

pygame.init()
display_window = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Rect Object & Text')

txt = pygame.font.SysFont('Times New Roman', 20)
txtobj = txt.render('This is a red rectangle', True, (255, 255, 255), (255, 0, 0))
txtrect = txtobj.get_rect()
txtrect.topleft = (40, 150)  # Position the text below the rectangle

while True:
    for each_event in pygame.event.get():
        if each_event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    display_window.fill((0, 0, 0))  # Clear the screen with black before drawing

    pygame.draw.rect(display_window, (255, 0, 0), pygame.Rect(40, 30, 100, 100))
    display_window.blit(txtobj, txtrect)

    pygame.display.flip()
