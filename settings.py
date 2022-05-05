import pygame as pg

WIDTH = pg.display.set_mode().get_width()
HEIGHT = pg.display.set_mode().get_height()

SLOVAK_ALPHABET = 'aáäbcčdďdzdžeéfghhiíjklĺľmnňoóôpqrŕsštťuúvwxyýzž'
SYMBOLS = ",.-'!?@#$%^&*()+=/\\"
NUMBERS = '1234567890'

hearts_count = 5
small_button_width = WIDTH // 5
big_button_width = WIDTH // 4
