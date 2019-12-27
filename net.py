import pygame
"""Net class """
class Net():

    def __init__(self, image, xcoor, ycoor, screen):
        self.screen = screen #screen info

        self.image = pygame.image.load(image) #load the image
        self.rect = self.image.get_rect()

        self.rect.centerx = xcoor #set x coordinate
        self.rect.centery = ycoor #set y coordinate


    def blitme(self):
        self.screen.blit(self.image, self.rect) #draws the net
