import pygame
""" Player class """
class Player():

    def __init__(self, os_settings, screen, image, xpos):

     self.screen = screen #get the screen object

     #Load the plyaer image and get its rect function
     self.image = pygame.image.load(image)
     self.rect = self.image.get_rect()

     self.initxpos = xpos #intial x position for resetting purposes
     self.initypos = os_settings.ground_level #intial  yposition for resetting purposes
     self.rect.centerx = xpos #intialize starting point
     self.rect.centery = os_settings.ground_level #ground level

     self.moving_right = False #movement flag for mobving right
     self.moving_left = False #movement flag for moving left
     self.jumping = False #movement flag for jumping

     self.direction = 0 #direction of the player 1 is right -1 is left
     self.xvelocity = os_settings.player_xvelocity
     self.yvelocity = os_settings.player_yvelocity
     self.yacceleration = os_settings.player_yacceleration

    def reset(self): #reset player's position
        self.rect.centerx = self.initxpos
        self.rect.centery = self.initypos
        self.direction = 0
        self.jumping = False

    def update(self, os_settings): #basic movement of the player
        if self.moving_right and self.rect.right < os_settings.screen_limit_right: #update position based on the movment flag
            self.rect.centerx += self.xvelocity #move to the right
            self.direction = 1

        if self.moving_left and self.rect.left > os_settings.screen_limit_left: #moving left
            self.rect.centerx -= self.xvelocity #move to the left
            self.direction = -1

        if self.jumping: #jumping
            self.rect.centery -= self.yvelocity
            self.yvelocity += self.yacceleration
            if self.rect.centery == os_settings.ground_level: #don't go below ground level
                self.yvelocity = 0
                self.jumping = False


    def blitme(self):
        self.screen.blit(self.image, self.rect) #draws the player
