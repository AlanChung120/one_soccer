import sys
import pygame
import random
import time
""" Game functions for interaction between objects, player and the computer """
def check_events(os_settings, player1, player2, soccer_ball, stats, play_button, clock, sb): #responds to keypresses and mouse events
    for event in pygame.event.get(): #watch for keyboard and mouse events
        if event.type == pygame.QUIT: #quit button will exit the game
            sys.exit()
        elif event.type == pygame.KEYDOWN: #check key down event
            check_keydown_events(os_settings, event, player1, player2)
        elif event.type == pygame.KEYUP: #check key up events
            check_keyup_events(event, player1, player2)
        elif event.type == pygame.MOUSEBUTTONDOWN: #if the user presses down on their mouse
            mouse_x, mouse_y = pygame.mouse.get_pos() #get the mouse cursor posisition
            check_play_button(os_settings, stats, play_button, mouse_x, mouse_y, player1, player2, soccer_ball, clock, sb) #runs the play button click check method

def check_keydown_events(os_settings, event, player1, player2):
    #player 1 keys
    if event.key == pygame.K_RIGHT: #move right
        player1.moving_right = True
    if event.key == pygame.K_LEFT: #move left
        player1.moving_left = True
    if event.key == pygame.K_UP and player1.rect.centery == os_settings.ground_level: #jump
        player1.yvelocity = os_settings.player_yvelocity
        player1.jumping = True
    #player 2 keys
    if event.key == pygame.K_d: #move right
        player2.moving_right = True
    if event.key == pygame.K_a: #move left
        player2.moving_left = True
    if event.key == pygame.K_w and player2.rect.centery == os_settings.ground_level: #jump
        player2.yvelocity = os_settings.player_yvelocity
        player2.jumping = True


def check_keyup_events(event, player1, player2):
    #player 1 keys
    if event.key == pygame.K_RIGHT: #stopping moving to the right
        player1.moving_right = False
    if event.key == pygame.K_LEFT:
        player1.moving_left = False
    #player 2 key up event
    if event.key == pygame.K_d:
        player2.moving_right = False
    if event.key == pygame.K_a:
        player2.moving_left = False

def check_play_button(os_settings, stats, play_button, mouse_x, mouse_y, player1, player2, soccer_ball, clock, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    #play the game
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        sb.prep_onescore()
        sb.prep_twoscore()
        clock.tick()
        stats.game_active = True
        reset_game(os_settings, player1, player2, soccer_ball)


def update_player1(os_settings, player1, player2):
    player1.update(os_settings) #update player 1

    if player1.rect.colliderect(player2.rect): #collision block
        if player1.direction == 1 and player1.rect.left > os_settings.screen_limit_left: #when moving right
            player1.rect.centerx -= player1.xvelocity

        if player1.direction == -1 and player1.rect.right < os_settings.screen_limit_right: #when moving left
            player1.rect.centerx += player1.xvelocity

def update_player2(os_settings, player1, player2):
    player2.update(os_settings) #update player 2

    if player2.rect.colliderect(player1.rect): #collision block
        if player2.direction == 1 and player2.rect.left > os_settings.screen_limit_left: #when moving right
            player2.rect.centerx -= player2.xvelocity

        if player2.direction == -1 and player2.rect.right < os_settings.screen_limit_right: #when moving left
            player2.rect.centerx += player2.xvelocity

def update_ball(os_settings, soccer_ball, player1, player2, stats, sb): #ball update
    soccer_ball.update(os_settings) #update ball
    if soccer_ball.rect.colliderect(player1.rect): #collision with player1
        if soccer_ball.rect.bottom - player1.rect.top < 3: #check if player is heading the ball
            ball_upward(os_settings, player1, soccer_ball) #vertical ball movement
        else:
            ball_xmovement(os_settings, player1, soccer_ball) #both horizontal and vertical ball movement
            ball_ymovement(player1, soccer_ball)

    if soccer_ball.rect.colliderect(player2.rect): #collision with player2
        if soccer_ball.rect.bottom - player2.rect.top < 3: #check if player is heading the ball
            ball_upward(os_settings, player2, soccer_ball) #vertical ball movement
        else:
            ball_xmovement(os_settings, player2, soccer_ball) #both horizontal and vertical ball movement
            ball_ymovement(player2, soccer_ball)

    if crossbar_collision(os_settings, soccer_ball): #collision with crossbar
        soccer_ball.direction = soccer_ball.direction * -1 #change direction

    if check_goal(os_settings, soccer_ball, stats, sb): #if scored
        reset_game(os_settings, player1, player2, soccer_ball) #reset position

def ball_xmovement(os_settings, player, soccer_ball): #xmovement when in contact of player
    if soccer_ball.rect.centerx > player.rect.centerx: #if ball is on the right
        soccer_ball.direction = 1
        soccer_ball.xvelocity = os_settings.ball_kick_velocity
    elif soccer_ball.rect.centerx < player.rect.centerx: #if ball is on the right
        soccer_ball.direction = -1
        soccer_ball.xvelocity = os_settings.ball_kick_velocity

def ball_ymovement(player, soccer_ball): #ymovement when in contact of player
    if not soccer_ball.inair: #if on ground and not jumping (put "not player.jumping and" to disable air kick
        soccer_ball.inair = True #jump
        soccer_ball.yvelocity = random.randrange(5,8) #random number

def ball_upward(os_settings, player, soccer_ball): #heading to send the ball flying
    soccer_ball.inair = True
    soccer_ball.yvelocity = os_settings.ball_head_velocity

def crossbar_collision(os_settings, soccer_ball): #we're doing the average of two coordinates(crossbar bounce back)
    if soccer_ball.rect.centerx > os_settings.net_right_in and soccer_ball.rect.centery < os_settings.crossbar_height:
        return True

    if soccer_ball.rect.centerx < os_settings.net_left_in and soccer_ball.rect.centery < os_settings.crossbar_height:
        return True

def check_goal(os_settings, soccer_ball, stats, sb): #check if the ball goes in the net
    if soccer_ball.rect.centerx > os_settings.net_right_in and soccer_ball.rect.centery > os_settings.crossbar_height:
        stats.onescore += 1
        sb.prep_onescore()
        return True
    if soccer_ball.rect.centerx < os_settings.net_left_in and soccer_ball.rect.centery > os_settings.crossbar_height:
        stats.twoscore += 1
        sb.prep_twoscore()
        return True

def reset_game(os_settings, player1, player2, soccer_ball): #reset when goal
    player1.reset() #reset player positions
    player2.reset()
    soccer_ball.reset() #reset ball position

def countdown(stats, clock, sb): #countdown the time
    if stats.milliseconds < 0: #reset millisecond
        stats.seconds -= 1
        stats.milliseconds += 1000
        sb.prep_timer()
    if stats.seconds < 0: #reset seconds
        stats.minutes -= 1
        stats.seconds += 60
        sb.prep_timer()
    if stats.minutes < 0: #restart game
        stats.game_active = False
        stats.minutes = 0
        stats.seconds = 0
        stats.milliseconds = 0
        sb.prep_timer()
        pygame.mouse.set_visible(True)
        game_winner(stats, sb)

    if stats.minutes >= 0:
        stats.milliseconds -= clock.tick(500)

def game_winner(stats, sb): #display the winner
    if stats.onescore > stats.twoscore:
        sb.prep_winner("Player 1 Wins", (0,0,100))

    elif stats.twoscore > stats.onescore:
        sb.prep_winner("Player 2 Wins", (100,0,0) )

    else:
        sb.prep_winner("Tie", (0,0,0))



def update_screen(os_settings, screen, player1, player2, background, net_right, net_left, soccer_ball, stats, play_button, sb):
    screen.blit(background.image, background.rect) #show the background
    soccer_ball.blitme() #draw ball
    net_right.blitme() #draw net
    net_left.blitme()
    player1.blitme() #draw player 1
    player2.blitme() #draw player 2
    sb.show_score() #show scoreboard
    if not stats.game_active:
        play_button.draw_button()
        sb.show_winner()
    pygame.display.flip() #make the most recently drawn screen visible
