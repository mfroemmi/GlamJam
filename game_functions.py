import random
import sys
import pygame
import time

from life import Life

def check_keydown_events(ai_settings, event, player):
    if event.key == pygame.K_RIGHT:
        ai_settings.collide_left = False
        ai_settings.collide_top = False
        ai_settings.collide_bottom = False
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        ai_settings.collide_right = False
        ai_settings.collide_top = False
        ai_settings.collide_bottom = False
        player.moving_left = True
    elif event.key == pygame.K_UP:
        ai_settings.collide_left = False
        ai_settings.collide_right = False
        ai_settings.collide_top = False
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        ai_settings.collide_left = False
        ai_settings.collide_right = False
        ai_settings.collide_bottom = False
        player.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(ai_settings, event, player):
    if event.key == pygame.K_RIGHT:
        ai_settings.collide_left = False
        ai_settings.collide_right = False
        ai_settings.collide_top = False
        ai_settings.collide_bottom = False
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        ai_settings.collide_left = False
        ai_settings.collide_right = False
        ai_settings.collide_top = False
        ai_settings.collide_bottom = False
        player.moving_left = False
    elif event.key == pygame.K_UP:
        ai_settings.collide_left = False
        ai_settings.collide_right = False
        ai_settings.collide_top = False
        ai_settings.collide_bottom = False
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        ai_settings.collide_left = False
        ai_settings.collide_right = False
        ai_settings.collide_top = False
        ai_settings.collide_bottom = False
        player.moving_down = False

def check_events(ai_settings, player):
    # Reaktion auf Tastaturaufgaben
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, event, player)

        elif event.type == pygame.KEYUP:
            check_keyup_events(ai_settings, event, player)

def check_player_hit(ai_settings, screen, player, lifes, enemy, enemy2, enemy3):
    if pygame.sprite.collide_rect(player, enemy):
        ai_settings.player_life -= 1
        update_life(ai_settings, screen, lifes)
        ai_settings.starttime = time.process_time()
    if pygame.sprite.collide_rect(player, enemy2):
        ai_settings.player_life -= 1
        update_life(ai_settings, screen, lifes)
        ai_settings.starttime = time.process_time()
    if pygame.sprite.collide_rect(player, enemy3):
        ai_settings.player_life -= 1
        update_life(ai_settings, screen, lifes)
        ai_settings.starttime = time.process_time()

# Checkt ob der Spieler den Punkt eingesammelt hat
def check_point_collect(ai_settings, ai_settings2, ai_settings3, player, point, scoreboard, speed, level, block1, block2, block3):
    if pygame.sprite.collide_rect(player, point):
        point.rect.centerx = ai_settings.randomx = random.randint(ai_settings.random_screen_xstart,
                                                                  ai_settings.random_screen_xend)
        point.rect.centery = ai_settings.randomy = random.randint(ai_settings.random_screen_ystart,
                                                                  ai_settings.random_screen_yend)

        # Speichert ein Fließkommawert für die Spielermitte
        point.centerx = float(point.rect.centerx)
        point.centery = float(point.rect.centery)

        if pygame.sprite.collide_rect(point, block1) or pygame.sprite.collide_rect(point, block2) or pygame.sprite.collide_rect(point, block3):
            point.rect.centerx = ai_settings.randomx = random.randint(ai_settings.random_screen_xstart,
                                                                      ai_settings.random_screen_xend)
            point.rect.centery = ai_settings.randomy = random.randint(ai_settings.random_screen_ystart,
                                                                      ai_settings.random_screen_yend)

            # Speichert ein Fließkommawert für die Spielermitte
            point.centerx = float(point.rect.centerx)
            point.centery = float(point.rect.centery)

        else:
            score_up(ai_settings, ai_settings2, ai_settings3, speed, scoreboard, level)


def score_up(ai_settings, ai_settings2, ai_settings3, speed, scoreboard, level):
    ai_settings.score += 1 * ai_settings.game_speed
    ai_settings.game_speed = ai_settings.game_speed * ai_settings.game_speed_factor
    ai_settings.enemy_speed_factor = ai_settings.game_speed
    ai_settings2.enemy_speed_factor = ai_settings.game_speed
    ai_settings3.enemy_speed_factor = ai_settings.game_speed
    speed.prep_speed()
    scoreboard.prep_score()
    level.prep_level()

def create_enemy(ai_settings, ai_settings2, ai_settings3, enemy, enemy2, enemy3):
    # Legt die Startbedigungen der einzelnen Gegner fest
    # Gegner 1
    enemy.centerx += 100
    enemy.centery += 100
    ai_settings.enemy_direction = 2
    ai_settings.enemy_direction_factorx = 1
    ai_settings.enemy_direction_factory = 1

    # Gegner 2
    enemy2.centerx -= 90
    enemy2.centery -= 90
    ai_settings2.enemy_direction = 3
    ai_settings2.enemy_direction_factorx = -1
    ai_settings2.enemy_direction_factory = 1

    # Gegner 3
    enemy3.centerx += 95
    enemy3.centery -= 95
    ai_settings3.enemy_direction = 1
    ai_settings3.enemy_direction_factorx = 1
    ai_settings3.enemy_direction_factory = -1

# Erstellt die Leben zu beginn des Spiels
def create_life(ai_settings, screen, lifes):

    for number_life in range(ai_settings.player_life):
        life = Life(ai_settings, screen)
        life.rect.centerx += 30 * number_life
        life.centerx = life.rect.centerx
        lifes.add(life)

# Update der Leben nach einem Treffer
def update_life(ai_settings, screen, lifes):
    lifes.empty()

    for number_life in range(ai_settings.player_life):
        life = Life(ai_settings, screen)
        life.rect.centerx += 30 * number_life
        life.centerx = life.rect.centerx
        lifes.add(life)

def check_life(ai_settings):
    if ai_settings.player_life <= 0:
        ai_settings.game_aktive = False

def create_block(ai_settings, block1, block2, block3):
    # Mischt die Positionsangaben der Blöcke
    random.shuffle(ai_settings.block_posx)
    random.shuffle(ai_settings.block_posy)

    # Lädt alle Bilder
    block2.image = ai_settings.block2
    block3.image = ai_settings.block3

    block2.rect = block2.image.get_rect()
    block3.rect = block3.image.get_rect()

    # Weist den Blöcken die Startpositionen zu
    block1.rect.centerx = ai_settings.block_posx[0]
    block1.rect.centery = ai_settings.block_posy[0]

    block2.rect.centerx = ai_settings.block_posx[1]
    block2.rect.centery = ai_settings.block_posy[1]

    block3.rect.centerx = ai_settings.block_posx[2]
    block3.rect.centery = ai_settings.block_posy[2]

    # Speichert die Positionen in Fließkommawerte
    block1.centerx = float(block1.rect.centerx)
    block1.centery = float(block1.rect.centery)

    block2.centerx = float(block2.rect.centerx)
    block2.centery = float(block2.rect.centery)

    block3.centerx = float(block3.rect.centerx)
    block3.centery = float(block3.rect.centery)

def update_screen(ai_settings, screen, player, point, scoreboard, speed, level, lifes, enemy, enemy2, enemy3, block1, block2, block3, field, gameover):
    # Zeichnet den Bildschirm bei jedem Schleifendurchlauf neu
    screen.fill(ai_settings.bg_color)

    if not ai_settings.game_aktive:
        gameover.show_game_over()

    # Zeichnet den Spieler auf den Bildschirm
    player.blit()

    # Zeichnet den Punkt auf den Bildschirm
    point.blit()

    # Zeichnet die Gegner auf den Bildschirm
    enemy.blit()
    enemy2.blit()
    enemy3.blit()

    # Zeichnet die Blöcke
    block1.blit()
    block2.blit()
    block3.blit()

    # Zeichnet das Feld auf den Bildschirm
    field.blit()

    # Zeichnet das Scoreboard
    scoreboard.show_score()

    # Zeichnet die Spielgeschwindigkeitsanzeige
    speed.show_speed()

    # Zeichnet die Levelanzeige
    level.show_level()

    # Zeichnet die Lebenspunkte
    lifes.draw(screen)

    # Macht den zuletzt gezeichneten Bildschirm sichtbar
    pygame.display.flip()

    time.sleep(0.001)