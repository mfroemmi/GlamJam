import pygame

class Field():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Lädt das bild des Spielers und ruft dessen umgebendes rechteck ab
        self.image = pygame.image.load('rsc/field.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Platziert den Spieler in der mitte des Spielfeldes
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blit(self):
        # Zeichnet den Spieler an der Position von rect
        self.screen.blit(self.image, self.rect)