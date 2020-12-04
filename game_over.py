import pygame.font

class Gameover():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Legt die Abmessungen und Eigenschafften der Schaltfläche fest
        self.text_color = (60, 254, 0)
        self.font = pygame.font.Font("rsc/calibri.ttf", 60)

        # Richtet das Anfangsbild für den Punktestand ein
        self.prep_game_over() # Wandelt den Text in ein Bild um

    def prep_game_over(self):
        self.score_image = self.font.render(self.ai_settings.game_over, True, self.text_color, None)

        # Zeigt den Punktestand oben rechts auf dem Bildschirm an
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.centery = self.screen_rect.centery

    def show_game_over(self):
        self.screen.blit(self.score_image, self.score_rect)