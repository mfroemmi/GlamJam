import random

import pygame

class Point():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Lädt das bild des Spielers und ruft dessen umgebendes rechteck ab
        self.image = pygame.image.load('rsc/point.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Platziert den Spieler in der mitte des Spielfeldes
        self.rect.centerx = ai_settings.randomx = random.randint(ai_settings.random_screen_xstart, ai_settings.random_screen_xend)
        self.rect.centery = ai_settings.randomy = random.randint(ai_settings.random_screen_ystart, ai_settings.random_screen_yend)

        # Speichert ein Fließkommawert für die Spielermitte
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blit(self):
        # Zeichnet den Gegner an der Position von rect
        self.screen.blit(self.image, self.rect)