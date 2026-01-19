import pygame as pg
import time

pg.mixer.init()
pg.mixer.music.load('mp3sound.mp3')
pg.mixer.music.play()



while pg.mixer.music.get_busy():
    time.sleep(1)