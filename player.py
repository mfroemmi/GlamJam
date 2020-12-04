import pygame

class Player():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Lädt das bild des Spielers und ruft dessen umgebendes rechteck ab
        self.image = pygame.image.load('rsc/player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Platziert den Spieler in der mitte des Spielfeldes
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Speichert ein Fließkommawert für die Spielermitte
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Bewegungsflag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blit(self):
        # Zeichnet den Spieler an der Position von rect
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Aktualisierung der Spielerposition
        if self.moving_right and self.rect.right < (self.screen_rect.right - self.ai_settings.correct_left_top_right) and not self.ai_settings.collide_left:
            self.centerx += self.ai_settings.player_speed_factor
        if self.moving_left and self.rect.left > (0 + self.ai_settings.correct_left_top_right) and not self.ai_settings.collide_right:
            self.centerx -= self.ai_settings.player_speed_factor
        if self.moving_up and self.rect.top > (0 + self.ai_settings.correct_left_top_right) and not self.ai_settings.collide_bottom:
            self.centery -= self.ai_settings.player_speed_factor
        if self.moving_down and self.rect.bottom < (self.screen_rect.bottom - self.ai_settings.correct_bottom) and not self.ai_settings.collide_top:
            self.centery += self.ai_settings.player_speed_factor

        # Aktualisiert das rect-Objekt auf Grundlage von self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
