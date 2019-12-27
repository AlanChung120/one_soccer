import pygame.font
from pygame.sprite import Group
""" Scoreboard class """
class Scoreboard():

    def __init__(self, screen, stats):
        """initialize score keeping attributes"""
        self.screen = screen #get screen object
        self.screen_rect = screen.get_rect() #get rect attribute
        self.stats = stats

        self.text_color = (0,0,0) #set up text color
        self.font = pygame.font.SysFont(None, 90) #set up font

        self.prep_onescore() #prepare the intial score image
        self.prep_twoscore()
        self.prep_winner("", (0,0,0))
        self.prep_timer()

    def prep_onescore(self): #prepare to display player1's score
        onescore_str = str(self.stats.onescore)
        self.onescore_image = self.font.render(onescore_str, True, self.text_color) #prep image

        self.onescore_rect = self.onescore_image.get_rect() #get the rect attribute for score's rect
        self.onescore_rect.left = self.screen_rect.left + 20
        self.onescore_rect.top = 20 #place it 20 pixels down from the top of the screen

    def prep_twoscore(self): #prepare to display player2's score
        twoscore_str = str(self.stats.twoscore)
        self.twoscore_image = self.font.render(twoscore_str, True, self.text_color) #prep image

        self.twoscore_rect = self.twoscore_image.get_rect() #get the rect attribute for score's rect
        self.twoscore_rect.right = self.screen_rect.right - 20 #place it 20 pixel from the right screen edge
        self.twoscore_rect.top = 20 #place it 20 pixels down from the top of the screen

    def prep_winner(self, winner, colour): #prepare to display the winner
        winner_str = str(winner)
        self.winner_image = self.font.render(winner_str, True, colour)

        self.winner_rect = self.winner_image.get_rect()
        self.winner_rect.centerx = self.screen_rect.centerx
        self.winner_rect.top = 150

    def prep_timer(self): #Intialize the timer
        timer = str("%02d:%02d" % (self.stats.minutes, self.stats.seconds)) #timer format
        self.timer_image = self.font.render(timer, True, self.text_color)

        self.timer_rect = self.timer_image.get_rect()
        self.timer_rect.centerx = self.screen_rect.centerx
        self.timer_rect.top = self.onescore_rect.top


    def show_score(self): #show each player's score and the timer
        self.screen.blit(self.onescore_image, self.onescore_rect)
        self.screen.blit(self.twoscore_image, self.twoscore_rect)
        self.screen.blit(self.timer_image, self.timer_rect)

    def show_winner(self): #display the winner
        self.screen.blit(self.winner_image, self.winner_rect)
