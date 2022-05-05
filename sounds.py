import pygame as pg

pg.mixer.init()

click_button = pg.mixer.Sound('sounds/click_button.mp3')
game_over = pg.mixer.Sound('sounds/game_over.mp3')
mistake = pg.mixer.Sound('sounds/mistake.mp3')
pause_on = pg.mixer.Sound('sounds/pause_on.mp3')
pause_off = pg.mixer.Sound('sounds/pause_off.mp3')
click_key = pg.mixer.Sound('sounds/click_key.wav')
countdown = pg.mixer.Sound('sounds/countdown.wav')
done = pg.mixer.Sound('sounds/done.wav')
game_start = pg.mixer.Sound('sounds/start.wav')
