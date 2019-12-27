import pygame
""" Ball class """
class Ball():

    def __init__(self, os_settings, screen, xcoor):

        self.screen = screen #get screen and setting object


        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()

        self.initxpos = xcoor #intial x position for resetting purposes
        self.initypos = os_settings.ground_level #intial y position for resetting purposes
        self.rect.centerx = xcoor #intialize starting point
        self.rect.centery = os_settings.ground_level

        self.inair = False #keep track of ball being in air

        self.xvelocity = 0
        self.yvelocity = 0
        self.direction = 0
        self.xacceleration = os_settings.ball_xacceleration
        self.yacceleration = os_settings.ball_yacceleration


    def reset(self):
        self.rect.centerx = self.initxpos
        self.rect.centery = self.initypos
        self.direction = 0
        self.inair = False

    def update(self, os_settings):
        screen_rect = self.screen.get_rect()
        if self.rect.right <= screen_rect.right and self.rect.left >= 0: #when inside the border
            self.rect.centerx += self.xvelocity * self.direction #ball movement
            if self.xvelocity >= 0: #if moving
                self.xvelocity += self.xacceleration #have deccelaration
                if self.xvelocity < 0: #if not moving(prevent negative velocity)
                    self.xvelocity = 0 #stop moving

        if self.inair: #if in air
            self.rect.centery -= self.yvelocity #go up
            self.yvelocity += self.yacceleration #slow down
            if self.rect.centery > os_settings.ground_level: #if below the ground
                self.yvelocity = 0 #stop velocity
                self.rect.centery = os_settings.ground_level #stop on ground
                self.inair = False #ball no longer in air




    def blitme(self):
        self.screen.blit(self.image, self.rect) #draws the ball
