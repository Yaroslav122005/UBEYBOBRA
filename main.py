import os
import random

import pygame
import sys
from random import randint, choice
import time
n = 0
lunki = [(30, 130), (180, 130), (330, 130), (30, 280), (180, 280), (330, 280), (30, 430), (180, 430), (330, 430)]
def load_image(name, colorkey=None):
    fullname = os.path.join('../UBEYBOBRA-main/data', name)
    image = pygame.image.load(fullname).convert()
    image.set_colorkey(colorkey)
    return image
pygame.init()
zawarudo = False
k = pygame.mixer.Sound('../UBEYBOBRA-main/data/norm_music.mp3')
k.play(-1)
sound = pygame.mixer.Sound('../UBEYBOBRA-main/data/shot.mp3')
zaw = pygame.mixer.Sound('../UBEYBOBRA-main/data/zaw.mp3')


pygame.time.set_timer(pygame.USEREVENT, 700)
font = pygame.font.SysFont('Consolas', 20)
win = pygame.display.set_mode((450, 550))
pygame.display.set_caption('Убей бобра (Играть со звуком!)')
hole_list = [False] * 9
dio = load_image("dio2.png")
clock = pygame.time.Clock()

score = 0

bobr = load_image("bobr_alive.jpg")
bobrs_list = [load_image("bobr_alive.jpg"), load_image("bobr_hunter.png"), load_image("bobr_murder.png"),
              load_image("bobr_battotai.png"), load_image("bobr_jeday.png"), load_image("bobr_soldier.png"),
              load_image("bobr_grenadier.png"), load_image("bobr_spec.png")]
hole_img = load_image("hole.png")
bg_img = load_image("BG.png")
top_bar = load_image("top_bar.png")
boss_img = load_image("BOSS.png")
krest = load_image('krest.png')
bobr_hole = 0
kill_boss = False
isBoss = False
krest = krest.convert()
colorkey = None
if colorkey is not None:
    krest = krest.convert()
    if colorkey == -1:
        colorkey = krest.get_at((0, 0))
    krest.set_colorkey(colorkey)
else:
    krest = krest.convert_alpha()
pygame.mouse.set_visible(False)
MANUAL_CURSOR = pygame.image.load('data/coursor.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT and not isBoss:
            if hole_list[bobr_hole]:
                score -= 1
                score = max(score, 0)
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
            hole_list[bobr_hole] = False
            new_bobr_hole = randint(0, 8)
            if new_bobr_hole == bobr_hole:
                bobr_hole = (new_bobr_hole + randint(0, 8)) % 8
            else:
                bobr_hole = new_bobr_hole
            bobr = choice(bobrs_list)
            hole_list[bobr_hole] = True

        if event.type == pygame.QUIT:
            sys.exit()



        if event.type == pygame.MOUSEBUTTONUP:
            sound.play()
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] in list(range(10, 60)) and mouse_pos[1] in list(range(10, 60)):
                pygame.quit()
                exit()
            if mouse_pos[0] in list(range(30, 120)) and mouse_pos[1] in list(range(130, 220)) and hole_list[0] and not isBoss:
                hole_list[0] = False
                score += 1

            elif mouse_pos[0] in list(range(180, 270)) and mouse_pos[1] in list(range(130, 220)) and hole_list[1] and not isBoss:
                hole_list[1] = False
                score += 1

            elif mouse_pos[0] in list(range(330, 420)) and mouse_pos[1] in list(range(130, 220)) and hole_list[2] and not isBoss:
                hole_list[2] = False
                score += 1

            elif mouse_pos[0] in list(range(30, 120)) and mouse_pos[1] in list(range(280, 370)) and hole_list[3] and not isBoss:
                hole_list[3] = False
                score += 1

            elif mouse_pos[0] in list(range(180, 270)) and mouse_pos[1] in list(range(280, 370)) and hole_list[4] and not isBoss:
                hole_list[4] = False
                score += 1

            elif mouse_pos[0] in list(range(330, 420)) and mouse_pos[1] in list(range(280, 370)) and hole_list[5] and not isBoss:
                hole_list[5] = False
                score += 1

            elif mouse_pos[0] in list(range(30, 120)) and mouse_pos[1] in list(range(430, 520)) and hole_list[6] and not isBoss:
                hole_list[6] = False
                score += 1

            elif mouse_pos[0] in list(range(180, 270)) and mouse_pos[1] in list(range(430, 520)) and hole_list[7] and not isBoss:
                hole_list[7] = False
                score += 1

            elif mouse_pos[0] in list(range(330, 420)) and mouse_pos[1] in list(range(430, 520)) and hole_list[8] and not isBoss:
                hole_list[8] = False
                score += 1

            elif not isBoss:
                score -= 1
            elif mouse_pos[0] in list(range(m[0], m[0] + 98)) and mouse_pos[1] in list(range(m[1], m[1] + 101)):
                score += 1
                if score == 20:
                    isBoss = False
                    pygame.mixer.music.load('../UBEYBOBRA-main/data/norm_music.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 40:
                    isBoss = False
                    pygame.mixer.music.load('../UBEYBOBRA-main/data/norm_music.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 60:
                    isBoss = False
                    pygame.mixer.music.load('../UBEYBOBRA-main/data/norm_music.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 80:
                    isBoss = False
                    pygame.mixer.music.load('../UBEYBOBRA-main/data/norm_music.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 100:
                    isBoss = False
                    pygame.mixer.music.load('../UBEYBOBRA-main/data/norm_music.mp3')
                    pygame.mixer.music.play(-1)
            score = max(score, 0)
            if score == 10 and not kill_boss:
                k.stop()
                pygame.time.set_timer(pygame.USEREVENT, 0)
                isBoss = True
                m = random.choice(lunki)
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
                if zawarudo:
                    pygame.mixer.music.play(-1)

            if score == 30:
                k.stop()
                pygame.time.set_timer(pygame.USEREVENT, 0)
                isBoss = True
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
                pygame.mixer.music.play(-1)

            if score == 50:
                k.stop()
                pygame.time.set_timer(pygame.USEREVENT, 0)
                isBoss = True
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
                pygame.mixer.music.play(-1)

            if score == 70:
                k.stop()
                pygame.time.set_timer(pygame.USEREVENT, 0)
                isBoss = True
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
                pygame.mixer.music.play(-1)

            if score == 90:
                k.stop()
                pygame.time.set_timer(pygame.USEREVENT, 0)
                isBoss = True
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
                pygame.mixer.music.play(-1)
            pygame.time.set_timer(pygame.USEREVENT, max(1000 - score * 2, 500))

    win.blit(bg_img, (0, 100))

    win.blit(top_bar, (0, 0))
    win.blit(krest, (10, 10))

    win.blit(font.render("Очки: " + str(score) + " (10=босс)", True, (0, 0, 0)), (100, 38))

    if not hole_list[0]:
        win.blit(hole_img, (30, 130))
    else:
        win.blit(bobr, (30, 130))

    if not hole_list[1]:
        win.blit(hole_img, (180, 130))
    else:
        win.blit(bobr, (180, 130))

    if not hole_list[2]:
        win.blit(hole_img, (330, 130))
    else:
        win.blit(bobr, (330, 130))

    if not hole_list[3]:
        win.blit(hole_img, (30, 280))
    else:
        win.blit(bobr, (30, 280))

    if not hole_list[4]:
        win.blit(hole_img, (180, 280))
    else:
        win.blit(bobr, (180, 280))

    if not hole_list[5]:
        win.blit(hole_img, (330, 280))
    else:
        win.blit(bobr, (330, 280))

    if not hole_list[6]:
        win.blit(hole_img, (30, 430))
    else:
        win.blit(bobr, (30, 430))

    if not hole_list[7]:
        win.blit(hole_img, (180, 430))
    else:
        win.blit(bobr, (180, 430))

    if not hole_list[8]:
        win.blit(hole_img, (330, 430))
    else:
        win.blit(bobr, (330, 430))

    if isBoss:
        #if score == 19:
            #if not zawarudo:
                #pygame.mixer.stop()
                #k.stop()
                #m = (0, 0)
                #win.blit(dio, m)
                #if n == 0:
                #    zaw.play(-1)
                #score %= 12
                #n += 1
        #else:
        win.blit(boss_img, m)

    if pygame.mouse.get_focused():
        win.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
