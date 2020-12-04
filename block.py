class Block():

    def __init__(self, ai_settings, screen, player):
        self.screen = screen
        self.ai_settings = ai_settings
        self.player = player

        # Lädt das bild des Spielers und ruft dessen umgebendes rechteck ab
        self.image = self.ai_settings.block1
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Platziert den Spieler in der mitte des Spielfeldes
        self.rect.centerx = self.ai_settings.block_posx[0]
        self.rect.centery = self.ai_settings.block_posy[0]

        # Speichert ein Fließkommawert für die Spielermitte
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blit(self):
        # Zeichnet den Gegner an der Position von rect
        self.screen.blit(self.image, self.rect)

    def update_collide_left(self):
        if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.top < self.rect.bottom and self.player.rect.bottom > self.rect.top and self.player.rect.centerx <= self.rect.left:
            self.ai_settings.collide_left = True

    def update_collide_right(self):
        if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.top < self.rect.bottom and self.player.rect.bottom > self.rect.top and self.player.rect.centerx >= self.rect.right:
            self.ai_settings.collide_right = True

    def update_collide_top(self):
        if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.top < self.rect.bottom and self.player.rect.bottom > self.rect.top and self.player.rect.centery <= self.rect.top:
            self.ai_settings.collide_top = True

    def update_collide_bottom(self):
        if self.player.rect.right > self.rect.left and self.player.rect.left < self.rect.right and self.player.rect.top < self.rect.bottom and self.player.rect.bottom > self.rect.top and self.player.rect.centery >= self.rect.bottom:
            self.ai_settings.collide_bottom = True