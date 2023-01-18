import os
from random import randint, choice
import cv2
import sys
import time
import pygame
video = cv2.VideoCapture("/data/123.avi")
success, video_image = video.read()
fps = video.get(cv2.CAP_PROP_FPS)
window = pygame.display.set_mode((450, 550))
clock = pygame.time.Clock()

run = success
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    success, video_image = video.read()
    if success:
        video_surf = pygame.image.frombuffer(
            video_image.tobytes(),
            video_image.shape[1::-1],
            "BGR"
        )
    else:
        run = False
    window.blit(video_surf, (0, 0))
    pygame.display.flip()

s = 0
def za_warudo():
    global score
    score = 11

n = 0
lunki = [(30, 130), (180, 130), (330, 130), (30, 280), (180, 280), (330, 280), (30, 430), (180, 430), (330, 430)]
def load_image(name, colorkey=None):
    fullname = os.path.join('../UBEYBOBRA-main/data', name)
    image = pygame.image.load(fullname).convert()
    image.set_colorkey(colorkey)
    return image
pygame.init()
zawarudo = True
import pygame, pyglet, ctypes

# setup pyglet & the video

k = pygame.mixer.Sound('../UBEYBOBRA-main/data/norm_music.mp3')
k.play(-1)
sound = pygame.mixer.Sound('../UBEYBOBRA-main/data/shot.mp3')
sound.set_volume(1.2)
zaw = pygame.mixer.Sound('../UBEYBOBRA-main/data/zaw.mp3')


pygame.time.set_timer(pygame.USEREVENT, 700)
font = pygame.font.SysFont('Consolas', 20)
win = pygame.display.set_mode((450, 550))
pygame.display.set_caption('Убей бобра (Играть со звуком!)')
hole_list = [False] * 9
dio = load_image("dio2.png")
score = 0

bobr = load_image("bobr_alive.jpg")
bobrs_list = [load_image("bobr_alive.jpg"), load_image("bobr_hunter.png"), load_image("bobr_murder.png"),
              load_image("bobr_battotai.png"), load_image("bobr_jeday.png"), load_image("bobr_soldier.png"),
              load_image("bobr_grenadier.png"), load_image("bobr_spec.png")]
hole_img = load_image("hole.png")
bg_img = load_image("BG.png")
top_bar = load_image("top_bar.png")
boss_img = load_image("BOSS.png")
bobr_hole = 0
kill_boss = False
isBoss = False
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


        if event.type == pygame.MOUSEBUTTONUP and zawarudo:
            sound.set_volume(0.2)
            sound.play()
            mouse_pos = pygame.mouse.get_pos()
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
                boss = time.time()
                m = random.choice(lunki)
                pygame.mixer.music.load('../UBEYBOBRA-main/data/BOSS_MUSIC.mp3')
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

    win.blit(font.render("Очки: " + str(score) + " (10=босс)" , True, (0, 0, 0)), (100, 38))

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
        if (time.time() - boss) % 2 <= 1:
            m = random.choice(lunki)
        win.blit(boss_img, m)
        if score == 19 and s == 0 or s == 1:
            win.blit(dio, (0, 0))
            zaw.play()
            if s == 0:
                x = time.time()
                s += 1
            if time.time() - x >= 4 and s == 1:
                za_warudo()
                s += 1
    if pygame.mouse.get_focused():
        win.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))
    pygame.display.flip()

pygame.quit()
