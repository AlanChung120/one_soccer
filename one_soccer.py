"""
Alan Chung
One Soccer (1 v 1 soccer game)
December 16th 2017
"""

import sys
import pygame
from background import Background
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
import time
from button import Button
from player import Player
from ball import Ball
from net import Net
import game_functions as gf

#main
def run_game():
    """ Intialize game and create a screen object """
    pygame.init()
    os_settings = Settings() #create a setting object
    screen = pygame.display.set_mode((os_settings.screen_width, os_settings.screen_height)) #screen size
    pygame.display.set_caption("One Soccer")
    clock = pygame.time.Clock()
    play_button = Button(os_settings, screen, "Play")
    stats = GameStats() #create stats object
    sb = Scoreboard(screen, stats) #create scoreboard object
    player1 = Player(os_settings, screen, "images/player1.png", os_settings.player1_xcoor) #create player 1
    player2 = Player(os_settings, screen, "images/player2.png", os_settings.player2_xcoor) #create player 2
    soccer_ball = Ball(os_settings, screen, os_settings.ball_xcoor) #create soccer ball
    #create nets
    net_left = Net("images/net1.png", os_settings.net_left_xcoor, os_settings.net_ycoor, screen)
    net_right = Net("images/net2.png", os_settings.net_right_xcoor, os_settings.net_ycoor, screen)
    background = Background("images/background.png", [0,0]) #set background picture


    #main loop for the game
    while True:
        gf.check_events(os_settings, player1, player2, soccer_ball, stats, play_button, clock, sb) #key press and mouse press event checking function from gf
        if stats.game_active:
            gf.update_player1(os_settings, player1, player2) #updating player 1
            gf.update_player2(os_settings, player1, player2) #updating player 2
            gf.countdown(stats, clock, sb) #Timer Countdown
            gf.update_ball(os_settings, soccer_ball, player1, player2, stats, sb) #updating ball movement
        gf.update_screen(os_settings, screen, player1, player2, background, net_right, net_left, soccer_ball, stats, play_button, sb) #update screen function from gf

run_game() #run game
