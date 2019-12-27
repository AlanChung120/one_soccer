import pygame.font
""" Button class """
class Button():

     def __init__(self, os_settings, screen, msg):

         self.screen = screen
         self.screen_rect = screen.get_rect() #get rect attribute

         self.button_color = (0,255,0) #set up button color
         self.text_color = (255,255,255) #set up text color
         self.font = pygame.font.SysFont(None, os_settings.button_font) #set up font

         self.rect = pygame.Rect(0, 0, os_settings.button_width, os_settings.button_height) #build the button's rect
         self.rect.center = self.screen_rect.center #put the button's rect in the middle

         self.prep_msg(msg) #prep message to handle rendering

     def prep_msg(self,msg): #renders the text in to an image and positions it accordingly
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #turns the text stored in msg in to an image
        #the true is for anti-aliasing which makes the edges smoother the rest is text color and bg color
        self.msg_image_rect = self.msg_image.get_rect() # get the rect from the image created from the msg text
        self.msg_image_rect.center = self.rect.center #center it

     def draw_button(self):
        self.screen.fill(self.button_color, self.rect) #draw the outside button
        self.screen.blit(self.msg_image, self.msg_image_rect) #draw the text image to the screen
