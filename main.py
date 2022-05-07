import pickle
import time
from random import randint

from leaderboard import Leader
from shortcuts import *
from sounds import *
from sprites import *

pg.init()
texts, buttons = list(), list()
screen = pg.display.set_mode((WIDTH, HEIGHT))

CURRENT_PAGE = 'main'
LEVEL = 0
started = False
pause = False
start = time.time()
username = 'player'


def display_items():
    for text in texts:
        text.draw(screen)
    for button in buttons:
        button.draw(screen)


def clear_items():
    buttons.clear()
    texts.clear()


def main_menu():
    global CURRENT_PAGE, started
    CURRENT_PAGE = 'main'
    started = False


def main_menu_screen():
    x_pos = (WIDTH - BIG_BUTTON_WIDTH) // 2
    y_pos = HEIGHT * 0.4
    padding = HEIGHT * 0.1
    texts.append(
        ColouredText(
            position=(0, HEIGHT * 0.2),
            text='TYPING SPEED TEST',
            color=(255, 0, 0),
            width_center=True,
            font_size=WIDTH // 15
        )
    )
    buttons.append(
        Button(
            position=(x_pos, y_pos),
            font_size=WIDTH // 30,
            text="PLAY",
            action=levels_list,
            width=BIG_BUTTON_WIDTH,
            levels_type='game'
        )
    )
    buttons.append(
        Button(
            position=(x_pos, y_pos + padding),
            font_size=WIDTH // 30,
            text="LEADERBOARD",
            action=levels_list,
            width=BIG_BUTTON_WIDTH,
            levels_type='leaderboard'
        )
    )
    buttons.append(
        Button(
            position=(x_pos, y_pos + padding * 2),
            font_size=WIDTH // 30,
            text="QUIT",
            action=exit,
            width=BIG_BUTTON_WIDTH
        )
    )


def levels_list(levels_type: str):
    global CURRENT_PAGE
    CURRENT_PAGE = f'levels_{levels_type}'


def levels_list_page(action):
    y_pos = HEIGHT * 0.2
    padding = HEIGHT * 0.09

    for x in (SMALL_BUTTON_WIDTH, WIDTH - SMALL_BUTTON_WIDTH * 2):
        for y in range(5):
            if len(buttons) < 5:
                buttons.append(
                    Button(
                        position=(x, y_pos + padding * y),
                        font_size=WIDTH // 30,
                        text=f"LEVEL {y + 1}",
                        action=action,
                        width=WIDTH // 5,
                        level=y + 1
                    )
                )
            else:
                buttons.append(
                    Button(
                        position=(x, y_pos + padding * y),
                        font_size=WIDTH // 30,
                        text=f"LEVEL {y + 6}",
                        action=action,
                        width=WIDTH // 5,
                        level=y + 6
                    )
                )

    buttons.append(
        Button(
            position=((WIDTH - BIG_BUTTON_WIDTH) // 2, y_pos + padding * 6),
            font_size=WIDTH // 30,
            text="MENU",
            action=main_menu,
            width=BIG_BUTTON_WIDTH
        )
    )


def generate_phrase(level: int) -> str:
    with open('Phrases/Slovak/dictionary.pickle', 'rb') as f:
        words = pickle.load(f)[level]
    return words[randint(0, len(words) - 1)]


def play(level):
    global CURRENT_PAGE, LEVEL
    CURRENT_PAGE = 'game'
    LEVEL = level


def leaderboard(level):
    global CURRENT_PAGE, LEVEL
    CURRENT_PAGE = 'leaderboard'
    LEVEL = level


def leaderboard_screen():
    with open(f'Leaderboards/level{LEVEL}.pickle', 'rb') as f:
        current_leaderboard = pickle.load(f)

    values = [
        'Username', 'Inputted phrases', 'Symbols per second', 'Hearts left', 'Typing efficiency', 'Score'
    ]

    width_padding = WIDTH * 0.14
    for idx, value in enumerate(values):
        texts.append(ColouredText(((idx + 1) * width_padding, HEIGHT * 0.1), value, (122, 122, 122), WIDTH // 60))

    height_padding = HEIGHT * 0.07
    for place in range(1, 11):
        if place == 1:
            screen.blit(gold, (WIDTH * 0.095, HEIGHT * 0.1 + height_padding * place))
        elif place == 2:
            screen.blit(silver, (WIDTH * 0.095, HEIGHT * 0.1 + height_padding * place))
        elif place == 3:
            screen.blit(bronze, (WIDTH * 0.095, HEIGHT * 0.1 + height_padding * place))
        else:
            texts.append(
                ColouredText(
                    position=(WIDTH * 0.1, HEIGHT * 0.1 + height_padding * place),
                    text=f'{place})',
                    color=(122, 122, 122),
                    font_size=WIDTH // 60
                )
            )
        if place in current_leaderboard:
            leader = current_leaderboard[place]
            texts.append(
                ColouredText(
                    position=(width_padding, HEIGHT * 0.1 + height_padding * place),
                    text=str(leader.username),
                    color=(122, 122, 122),
                    font_size=WIDTH // 60
                )
            )
            texts.append(
                ColouredText(
                    position=(2 * width_padding, HEIGHT * 0.1 + height_padding * place),
                    text=str(leader.inputted_phrases),
                    color=(122, 122, 122),
                    font_size=WIDTH // 60
                )
            )
            texts.append(
                ColouredText(
                    position=(3 * width_padding, HEIGHT * 0.1 + height_padding * place),
                    text=str(leader.symbols_per_second),
                    color=(122, 122, 122),
                    font_size=WIDTH // 60
                )
            )
            texts.append(
                ColouredText(
                    position=(4 * width_padding, HEIGHT * 0.1 + height_padding * place),
                    text=str(leader.hearts_left),
                    color=(122, 122, 122),
                    font_size=WIDTH // 60
                )
            )
            texts.append(
                ColouredText(
                    position=(5 * width_padding, HEIGHT * 0.1 + height_padding * place),
                    text=str(leader.input_efficiency),
                    color=(122, 122, 122),
                    font_size=WIDTH // 60))
            texts.append(
                ColouredText(
                    position=(6 * width_padding, HEIGHT * 0.1 + height_padding * place),
                    text=str(leader.score),
                    color=(122, 122, 122),
                    font_size=WIDTH // 60
                )
            )
        else:
            for i in range(6):
                texts.append(
                    ColouredText(
                        position=((i + 1) * width_padding, HEIGHT * 0.1 + height_padding * place),
                        text='-',
                        color=(122, 122, 122),
                        font_size=WIDTH // 60
                    )
                )
        buttons.append(
            Button(
                position=((WIDTH - BIG_BUTTON_WIDTH) // 2, HEIGHT * 0.9),
                font_size=WIDTH // 30,
                text="BACK",
                action=levels_list,
                width=BIG_BUTTON_WIDTH,
                levels_type='leaderboard'
            )
        )


def write_result():
    global CURRENT_PAGE
    CURRENT_PAGE = 'main'
    with open(f'Leaderboards/level{LEVEL}.pickle', 'rb') as f:
        current_leaderboard = pickle.load(f)
    leaders_list = list(current_leaderboard.values())
    efficiency = (count_of_symbols - len(mistakes)) / count_of_symbols if count_of_symbols else 0
    current_res = Leader(username, inputted_words, round(symbols_per_second, 2), HEARTS_COUNT - len(mistakes),
                         round(efficiency, 2), score)
    leaders_list.append(current_res)
    leaders_list = sorted(leaders_list, key=lambda leader: leader.score, reverse=True)[:10]
    new_leaderboard = dict()
    for idx, leader in enumerate(leaders_list):
        new_leaderboard[idx + 1] = leader
    with open(f'Leaderboards/level{LEVEL}.pickle', 'wb') as f:
        pickle.dump(new_leaderboard, f)


def is_in_top10():
    with open(f'Leaderboards/level{LEVEL}.pickle', 'rb') as f:
        current_leaderboard = pickle.load(f)
    leaders_list = list(current_leaderboard.values())
    if len(leaders_list) < 10:
        return True
    else:
        if score >= leaders_list[-1].score:
            return True
    return False


def result():
    global CURRENT_PAGE, username
    CURRENT_PAGE = 'result'
    username = 'player'


def result_screen():
    global username
    padding = HEIGHT * 0.1

    if is_in_top10():
        texts.append(ColouredText(
            position=(0, HEIGHT * 0.1),
            color=(255, 255, 0),
            text="CONGRATULATIONS",
            font_size=WIDTH // 30,
            width_center=True
        ))
        texts.append(ColouredText(
            position=(0, HEIGHT * 0.15),
            color=(255, 255, 0),
            text="YOU REACH TOP-10",
            font_size=WIDTH // 30,
            width_center=True
        ))

    texts.append(ColouredText(
        position=(0, HEIGHT * 0.3),
        color=(122, 122, 122),
        text=f"Inputted phrases: {inputted_words}",
        font_size=WIDTH // 40,
        width_center=True
    ))
    texts.append(ColouredText(
        position=(0, HEIGHT * 0.3 + padding * 0.5),
        color=(122, 122, 122),
        text=f"Symbols per second: {round(symbols_per_second, 2)}",
        font_size=WIDTH // 40,
        width_center=True
    ))
    texts.append(ColouredText(
        position=(0, HEIGHT * 0.3 + padding * 1),
        color=(122, 122, 122),
        text=f"Hearts left: {HEARTS_COUNT - len(mistakes)}",
        font_size=WIDTH // 40,
        width_center=True
    ))
    texts.append(ColouredText(
        position=(0, HEIGHT * 0.3 + padding * 1.5),
        color=(122, 122, 122),
        text=f"Typing efficiency: "
             f"{round((count_of_symbols - len(mistakes)) / count_of_symbols, 2) if count_of_symbols else 0}",
        font_size=WIDTH // 40,
        width_center=True
    ))
    texts.append(ColouredText(
        position=(0, HEIGHT * 0.3 + padding * 2),
        color=(122, 122, 122),
        text=f"Score: {score}",
        font_size=WIDTH // 40,
        width_center=True
    ))
    texts.append(ColouredText(
        position=(0, HEIGHT * 0.3 + padding * 3.5),
        color=(122, 122, 122),
        text=f"Press ENTER to continue",
        font_size=WIDTH // 40,
        width_center=True
    ))
    for menu_event in pg.event.get():
        if menu_event.type == pg.KEYDOWN:
            click_key.play()
            if is_in_top10():
                if pg.key.get_pressed()[pg.K_RETURN]:
                    write_result()
                elif pg.key.get_pressed()[pg.K_BACKSPACE]:
                    username = username[:-1]
                elif menu_event.unicode and len(username) < 15:
                    username += menu_event.unicode
            else:
                if pg.key.get_pressed()[pg.K_RETURN]:
                    main_menu()

    if is_in_top10():
        texts.append(ColouredText(
            position=(0, HEIGHT * 0.3 + padding * 2.5),
            color=(122, 122, 122),
            text=username,
            font_size=WIDTH // 40,
            width_center=True
        ))
        pg.draw.rect(surface=screen,
                     rect=pg.Rect(WIDTH // 3, HEIGHT * 0.3 + padding * 2.5,
                                  (WIDTH - 2 * WIDTH // 3),
                                  texts[-1].height), color=(255, 255, 255))


def count_score(hearts_left, inputted_phrases, symbols_per_sec, count_of_inputted_symbols):
    efficiency_of_input = (count_of_inputted_symbols - (HEARTS_COUNT - hearts_left)) / count_of_inputted_symbols \
        if count_of_inputted_symbols else 0
    return round(symbols_per_sec * (inputted_phrases + 1) * (1 + hearts_left / 10) * efficiency_of_input, 2)


def continue_game():
    global pause, start
    pause = False
    pause_off.play()
    start = time.time()


if __name__ == '__main__':
    mistakes = list()
    sound_mistakes = list()

    while True:
        clear_items()
        screen.fill((0, 0, 0))

        if CURRENT_PAGE == 'main':
            main_menu_screen()

        elif CURRENT_PAGE == 'levels_game':
            levels_list_page(play)

        elif CURRENT_PAGE == 'levels_leaderboard':
            levels_list_page(leaderboard)

        elif CURRENT_PAGE == 'leaderboard':
            leaderboard_screen()

        elif CURRENT_PAGE == 'game':
            if not started:
                mistakes.clear()
                time_left = 60
                inputted_text = ''
                start = time.time()
                symbols_per_second = 0.00
                count_of_symbols = 0
                inputted_words = 0
                score = 0
                generated_text = generate_phrase(LEVEL)
                colors_for_generated_text = [(122, 122, 122) for _ in generated_text]
                pause = False
                pause_duration = 0
                texts.append(
                    ColouredText((0, 0), 'PRESS SPACE TO START',
                                 (122, 122, 122), WIDTH // 30, width_center=True, height_center=True))
                texts.append(
                    ColouredText((0, HEIGHT * 0.55), 'SWITCH TO A SLOVAK KEYBOARD',
                                 (122, 122, 122), WIDTH // 50, width_center=True))
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if pg.key.get_pressed()[pg.K_SPACE]:
                            started = True
                            game_start.play()
            else:
                if pause:
                    buttons.append(
                        Button(position=((WIDTH - BIG_BUTTON_WIDTH) // 2, HEIGHT * 0.4),
                               text="MENU",
                               font_size=WIDTH // 30,
                               action=main_menu,
                               width=BIG_BUTTON_WIDTH
                               )
                    )
                    buttons.append(
                        Button(position=((WIDTH - BIG_BUTTON_WIDTH) // 2, HEIGHT * 0.5),
                               text="CONTINUE",
                               font_size=WIDTH // 30,
                               action=continue_game,
                               width=BIG_BUTTON_WIDTH
                               )
                    )
                else:
                    curr_time = str(round(time_left - (time.time() - start), 2))
                    if float(curr_time) != 60:
                        symbols_per_second = count_of_symbols / (60 - float(curr_time))

                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.unicode:
                                if event.unicode.lower() in SLOVAK_ALPHABET + SYMBOLS + NUMBERS or \
                                        pg.key.get_pressed()[pg.K_SPACE]:
                                    inputted_text += event.unicode
                                    count_of_symbols += 1
                            if pg.key.get_pressed()[pg.K_F1]:
                                pause_on.play()
                                pause = True
                                time_left = float(curr_time)

                    coloured_text = ColouredText(
                        position=(0, 0),
                        text=generated_text,
                        color=colors_for_generated_text,
                        font_size=WIDTH // 30
                    )
                    texts.append(
                        ColouredText(
                            position=(0, HEIGHT * 0.5),
                            text=generated_text,
                            color=colors_for_generated_text,
                            font_size=WIDTH // 30,
                            width_center=True
                        )
                    )
                    pg.draw.rect(
                        surface=screen,
                        rect=pg.Rect(WIDTH // 10, texts[-1].position[1] + HEIGHT // 10, (WIDTH - 2 * WIDTH // 10),
                                     texts[-1].height),
                        color=(255, 255, 255)
                    )
                    texts.append(
                        ColouredText(
                            position=(texts[-1].position[0], texts[-1].position[1] + HEIGHT // 10),
                            text=inputted_text,
                            color=(122, 122, 122),
                            font_size=WIDTH // 30
                        )
                    )

                    for idx, symbol in enumerate(inputted_text):
                        if symbol == generated_text[idx]:
                            colors_for_generated_text[idx] = (0, 255, 0)
                        else:
                            colors_for_generated_text[idx] = (255, 0, 0)
                    if inputted_text:
                        if inputted_text[-1] != generated_text[len(inputted_text) - 1]:
                            mistakes.append(inputted_text)
                            sound_mistakes = set(mistakes)
                            if len(mistakes) == len(sound_mistakes):
                                mistake.play()
                            mistakes = list(set(mistakes))

                    for i in range(HEARTS_COUNT - len(mistakes)):
                        screen.blit(heart, ((i + 1) * (WIDTH // 30), HEIGHT // 20))

                    if len(generated_text) == len(inputted_text):
                        inputted_text = ''
                        colors_for_generated_text = [(122, 122, 122) for _ in generated_text]
                        mistakes = [i for i in range(len(mistakes))]
                        inputted_words += 1
                        generated_text = generate_phrase(LEVEL)
                        colors_for_generated_text = [(122, 122, 122) for _ in generated_text]
                        done.play()

                    if len(mistakes) == HEARTS_COUNT or float(curr_time) == 0.00:
                        countdown.stop()
                        if len(mistakes) == HEARTS_COUNT:
                            game_over.play()
                        started = False
                        result()

                    score = count_score(5 - len(mistakes), inputted_words, symbols_per_second, count_of_symbols)

                    if float(curr_time) < 0:
                        curr_time = '0.00'
                    texts.append(
                        ColouredText((WIDTH * 0.03, HEIGHT * 0.1), curr_time,
                                     (122, 122, 122), WIDTH // 30))

                    symbols_per_second_text = f'Symbols/sec: {round(symbols_per_second, 2)}'
                    texts.append(
                        ColouredText(
                            position=(WIDTH * 0.75, HEIGHT * 0.05),
                            text=symbols_per_second_text,
                            color=(122, 122, 122),
                            font_size=WIDTH // 30
                        )
                    )
                    inputted_phrases_text = f'Inputted phrases: {inputted_words}'
                    texts.append(
                        ColouredText(
                            position=(WIDTH * 0.75, HEIGHT * 0.1),
                            text=inputted_phrases_text,
                            color=(122, 122, 122),
                            font_size=WIDTH // 30
                        )
                    )

                    score_text = f'Score: {score}'
                    texts.append(
                        ColouredText(
                            position=(WIDTH * 0.75, HEIGHT * 0.15),
                            text=score_text,
                            color=(122, 122, 122),
                            font_size=WIDTH // 30
                        )
                    )

                    texts.append(
                        ColouredText(
                            position=(0, HEIGHT * 0.75),
                            text='F1 - pause',
                            color=(122, 122, 122),
                            font_size=WIDTH // 35,
                            width_center=True
                        )
                    )

                    if float(curr_time) <= 4:
                        if started:
                            countdown.play()

        elif CURRENT_PAGE == 'result':
            result_screen()

        display_items()
        pg.display.update()
