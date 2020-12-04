import pygame


class Settings():

    def __init__(self):
        # Bildschirmeinstellungen
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (41, 41, 41)

        self.correct_left_top_right = 20
        self.correct_bottom = 100

        # Playereinstellungen
        self.player_speed_factor = 4
        self.player_life = 10
        self.player_points = 0

        # Punkteeinstellungen
        self.random_screen_xstart = 50
        self.random_screen_xend = 950
        self.random_screen_ystart = 50
        self.random_screen_yend = 650
        self.randomx = 0
        self.randomy = 0

        # Blockadeneinstellungen
        self.block1 = pygame.image.load('rsc/block1.png')
        self.block2 = pygame.image.load('rsc/block2.png')
        self.block3 = pygame.image.load('rsc/block3.png')
        self.block_posx = [300, 300, 700, 700]
        self.block_posy = [500, 150, 150, 500]

        self.collide_left = False
        self.collide_right = False
        self.collide_top = False
        self.collide_bottom = False

        # Gegnereinstellungen
        self.enemy_number = 3
        self.enemy_speed_factor = 1
        self.enemy_direction = 2 # Directions: 1=rechts-oben, 2=rechts-unten, 3=links-unten, 4=links-oben
        self.enemy_direction_factorx = 1
        self.enemy_direction_factory = 1

        # Zeiterfassung bei treffer eines Gegners
        self.starttime = 0

        # Spielstatistiken
        self.game_aktive = True
        self.game_over = "Game Over"
        self.score = 0
        self.game_speed_factor = 1.02
        self.game_speed = 1.0
        self.level = 1