import pygame.font

class Level():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Legt die Abmessungen und Eigenschafften der Schaltfläche fest
        self.text_color = (60, 254, 0)
        self.font = pygame.font.Font("rsc/calibri.ttf", 38)

        # Richtet das Anfangsbild für den Punktestand ein
        self.prep_level() # Wandelt den Text in ein Bild um

    def prep_level(self):
        score = int(self.ai_settings.game_speed)
        score_str = "{:,}".format(score)
        self.score_image = self.font.render("Lvl: " + score_str, True, self.text_color, None)

        # Zeigt den Punktestand oben rechts auf dem Bildschirm an
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.centerx - 40
        self.score_rect.bottom = self.screen_rect.bottom - 20

    def show_level(self):
        self.screen.blit(self.score_image, self.score_rect)