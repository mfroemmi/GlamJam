import pygame
import time

from pygame.sprite import Group
from pygame import mixer

from settings import Settings
from player import Player
from point import Point
from scoreboard import Scoreboard
from speed import Speed
from level import Level
from game_over import Gameover
from enemy import Enemy
from block import Block
from field import Field
import game_functions as gf

def run_game():

    #Initialisiert das Spiel und erstellt ein screen-Objekt
    pygame.init()

    # Das ist ein Test

    # Lädt die Hintergrundmusik
    mixer.music.load("rsc/music.wav")
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)

    # Erstellt eine Instanz von Settings
    ai_settings = Settings()
    ai_settings2 = Settings()
    ai_settings3 = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("GlamJam")

    # Erstellt eine Instanz von Player
    player = Player(ai_settings, screen)

    # Erstellt die Blöcke
    block1 = Block(ai_settings, screen, player)
    block2 = Block(ai_settings, screen, player)
    block3 = Block(ai_settings, screen, player)

    # Erstellt eine Instanz von Point
    point = Point(ai_settings, screen)

    # Erstellt das Scoreboard
    scoreboard = Scoreboard(ai_settings, screen)

    # Erstellt die Geschwindigkeitsanzeige
    speed = Speed(ai_settings, screen)

    # Erstellt die Levelanzeige
    level = Level(ai_settings, screen)

    gameover = Gameover(ai_settings, screen)

    # Erstellt eine Instanz von Field
    field = Field(ai_settings, screen)

    # Erstellt Instanzen der Gegner
    enemy = Enemy(ai_settings, screen)
    enemy2 = Enemy(ai_settings2, screen)
    enemy3 = Enemy(ai_settings3, screen)

    # Erstellt die Gruppe für Lebenspunkte
    lifes = Group()

    gf.create_life(ai_settings, screen, lifes)

    # Legt die Startbedigungen der einzelnen Gegner fest
    gf.create_enemy(ai_settings, ai_settings2, ai_settings3, enemy, enemy2, enemy3)

    # Legt die Startbedingungen der Blöcke fest
    gf.create_block(ai_settings, block1, block2, block3)

    # Startet die Hauptschleife des Spiels
    while True:
        # Setzt die Variable clock immer auf die aktuelle Prozesszeit
        clock = time.process_time()

        # Reagiert auf Tastatureingaben
        gf.check_events(ai_settings, player)

        # Checkt ob der Spieler getroffen wurde
        if (clock - ai_settings.starttime) >= 1: # Nach einem Treffer wird 1s gewartet bis erneut getroffen werden kann
            gf.check_player_hit(ai_settings, screen, player, lifes, enemy, enemy2, enemy3)

        # Checkt ob der Spieler den Punkt eingesammelt hat
        gf.check_point_collect(ai_settings, ai_settings2, ai_settings3, player, point, scoreboard, speed, level, block1, block2, block3)

        # Checkt ob der Spieler noch Leben hat
        gf.check_life(ai_settings)

        if ai_settings.game_aktive:
            # Update der Spielerposition und der Gegnerpositionen
            if pygame.sprite.collide_rect(player, block1):
                block1.update_collide_left()
                block1.update_collide_right()
                block1.update_collide_top()
                block1.update_collide_bottom()
            if pygame.sprite.collide_rect(player, block2):
                block2.update_collide_left()
                block2.update_collide_right()
                block2.update_collide_top()
                block2.update_collide_bottom()
            if pygame.sprite.collide_rect(player, block3):
                block3.update_collide_left()
                block3.update_collide_right()
                block3.update_collide_top()
                block3.update_collide_bottom()

            player.update()
            enemy.update()
            enemy2.update()
            enemy3.update()

        # Zeichnet den Bildschirm bei jedem Schleifendurchlauf neu
        # Macht den als letztes gezeichneten Bildschirm sichtbar
        gf.update_screen(ai_settings, screen, player, point, scoreboard, speed, level, lifes,  enemy, enemy2, enemy3, block1, block2, block3, field, gameover)

run_game()