import pygame
pygame.init()
white = (255, 255, 255)
display_surface = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Display Image!')

image_name = pygame.image.load(r'D:\Study Stuff\College\Projects\Pygame\image.jpg')

while True:
    display_surface.fill(white)
    display_surface.blit(image_name, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()