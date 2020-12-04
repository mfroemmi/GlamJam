import pygame
from pygame.sprite import Sprite


class Life(Sprite):

    def __init__(self, ai_settings, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Lädt das bild des Spielers und ruft dessen umgebendes rechteck ab
        self.image = pygame.image.load('rsc/life.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Platziert den Spieler in der mitte des Spielfeldes
        self.rect.centerx = 30
        self.rect.centery = self.ai_settings.screen_height - 70

        # Speichert ein Fließkommawert für die Spielermitte
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blit(self):
        # Zeichnet den Spieler an der Position von rect
        self.screen.blit(self.image, self.rect)