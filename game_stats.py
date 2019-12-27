""" GameStats class """
class GameStats():
    """Track statisitics for One Soccer"""
    def __init__(self):
        self.reset_stats()
        self.game_active = False #game is not active until play button is clicked

    def reset_stats(self): #intialize stats that can be changed during the game
        self.onescore = 0 #reset the player1 score to 0
        self.twoscore = 0 #reset the player2 score to 0
        self.milliseconds = 0
        self.seconds = 30
        self.minutes = 1 #timer back to 1 minute and 30 seconds
