import pygame.font
class Button():
    def __init__(self, Invad_set, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height =200,50
        self.b_color = (51,161,201)
        self.t_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg, True, self.t_color, self.b_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_b(self):
        self.screen.fill(self.b_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)        
