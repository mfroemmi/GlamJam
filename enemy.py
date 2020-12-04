import pygame

class Enemy():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Lädt das bild des Gegners und ruft dessen umgebendes rechteck ab
        self.image = pygame.image.load('rsc/enemy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Platziert den Gegner
        self.rect.centerx = self.screen_rect.centerx + 30
        self.rect.centery = self.screen_rect.centery + 30

        # Speichert ein Fließkommawert für die Gegnermitte
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blit(self):
        # Zeichnet den Gegner an der Position von rect
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Richtungswechsel der Gegner wenn der Rand berührt wird
        # Gegen den Uhrzeigersinn
        if self.rect.bottom >= (self.screen_rect.bottom - self.ai_settings.correct_bottom) and self.ai_settings.enemy_direction == 2:
            self.ai_settings.enemy_direction = 1
            self.ai_settings.enemy_direction_factorx = 1
            self.ai_settings.enemy_direction_factory = -1
        if self.rect.right >= (self.screen_rect.right - self.ai_settings.correct_left_top_right) and self.ai_settings.enemy_direction == 1:
            self.ai_settings.enemy_direction = 4
            self.ai_settings.enemy_direction_factorx = -1
            self.ai_settings.enemy_direction_factory = -1
        if self.rect.top <= (self.screen_rect.top + self.ai_settings.correct_left_top_right) and self.ai_settings.enemy_direction == 4:
            self.ai_settings.enemy_direction = 3
            self.ai_settings.enemy_direction_factorx = -1
            self.ai_settings.enemy_direction_factory = 1
        if self.rect.left <= (self.screen_rect.left + self.ai_settings.correct_left_top_right) and self.ai_settings.enemy_direction == 3:
            self.ai_settings.enemy_direction = 2
            self.ai_settings.enemy_direction_factorx = 1
            self.ai_settings.enemy_direction_factory = 1
        # Im Uhrzeigersinn
        if self.rect.top <= (self.screen_rect.top + self.ai_settings.correct_left_top_right) and self.ai_settings.enemy_direction == 1:
            self.ai_settings.enemy_direction = 2
            self.ai_settings.enemy_direction_factorx = 1
            self.ai_settings.enemy_direction_factory = 1
        if self.rect.right >= (self.screen_rect.right - self.ai_settings.correct_left_top_right) and self.ai_settings.enemy_direction == 2:
            self.ai_settings.enemy_direction = 3
            self.ai_settings.enemy_direction_factorx = -1
            self.ai_settings.enemy_direction_factory = 1
        if self.rect.bottom >= (self.screen_rect.bottom - self.ai_settings.correct_bottom) and self.ai_settings.enemy_direction == 3:
            self.ai_settings.enemy_direction = 4
            self.ai_settings.enemy_direction_factorx = -1
            self.ai_settings.enemy_direction_factory = -1
        if self.rect.left <= (self.screen_rect.left + self.ai_settings.correct_left_top_right) and self.ai_settings.enemy_direction == 4:
            self.ai_settings.enemy_direction = 1
            self.ai_settings.enemy_direction_factorx = 1
            self.ai_settings.enemy_direction_factory = -1

        self.centerx += self.ai_settings.enemy_speed_factor * self.ai_settings.enemy_direction_factorx
        self.centery += self.ai_settings.enemy_speed_factor * self.ai_settings.enemy_direction_factory

        # Aktualisiert das rect-Objekt auf Grundlage von self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery