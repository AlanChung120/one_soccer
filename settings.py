"""Setting class"""
class Settings():
    """Store all settings for One Soccer"""
#store all the varible here
    def __init__(self):
        """Screen settings """
        self.screen_width = 1329 #screen width
        self.screen_height = 735 #screen height
        self.screen_limit_left = 29 #player's movement limit for left side
        self.screen_limit_right = 1300 #player's movement limit for right side

        """ Button settings """
        self.button_height = 50 #set up play button height
        self.button_width = 200 #set up play button width
        self.button_font = 48 #set up the play button font size

        """Net settings """
        self.net_left_xcoor = 19 #left net x coordinate
        self.net_right_xcoor = 1310 #Right net x coordinate
        self.net_ycoor = 520 #net y coordinate
        self.crossbar_height = 434 #crossbar height
        self.net_left_in = 50 #left net goal line
        self.net_right_in = 1271 #right net goal line


        """ Ball settings """
        self.ball_xcoor = 667 #ball intial x coordinate
        self.ball_xacceleration = -0.1 #ball x acceleration
        self.ball_yacceleration = -0.25 #ball y acceleration
        self.ball_kick_velocity = 9 #ball's x velocity when kicked
        self.ball_head_velocity = 7 #ball's y velocity when headed

        """ Player settings """
        self.player1_xcoor = 525 #player 1 intial x coordinate
        self.player2_xcoor = 810 #player 2 inital x coordinate
        self.player_xvelocity = 3 #player x velocity
        self.player_yvelocity = 5 #player y velocity
        self.player_yacceleration = -0.15 #player y acceleration

        self.ground_level = 595 #The ground level
