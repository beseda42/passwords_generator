import pygame
import sys
import time

from pygame import KEYDOWN

from button import button_class
from functions import generate_passwords

#инициализация
pygame.init()

#размер экрана
width, height = 1024, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("генератор паролей")

#фоны
background_main = pygame.image.load("backgrounds/background_main.png")
background_settings = pygame.image.load("backgrounds/background_settings.png")


def main_menu():
    '''функция окна главного меню'''

    #создание кнопок
    title_button = button_class(30, 450, 754, 45, "", "buttons/title.png", "buttons/title_hover.png")
    start_button = button_class(30, 550, 721, 45, "", "buttons/start.png", "buttons/start_hover.png")
    exit_button = button_class(30, 650, 231, 45, "", "buttons/exit.png", "buttons/exit_hover.png")
    buttons_list = [title_button, start_button, exit_button]

    running = True
    while running:
        #вывод фон
        screen.fill((0, 0, 0))
        screen.blit(background_main, (0, 0))

        #вывод кнопок
        for buttons in buttons_list:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        #действия
        for event in pygame.event.get():
            #кнопки
            for buttons in buttons_list:
                buttons.handle_event(event)

            #закрытие игры
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            #кнопка выхода
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            #кнопка старта
            if event.type == pygame.USEREVENT and event.button == start_button:
                settings()

        pygame.display.flip()

def settings():
    '''функция окна настроек'''

    #объявление переменных
    n = "1" #количество паролей
    length = "1" #длина пароля
    letters = False #используются ли буквы
    register_up = False #используется ли верхний регистр
    register_down = False #используется ли нижний регистр
    register = 0 #1-только верхний, 2-только нижний, 3-оба
    numbers = False #используются ли цифры
    replaces = False #есть ли замены букв на слова
    specials = False #есть ли спец символы
    dict_eng = False #есть ли английские слова
    dict_ru = False #есть ли русские слова (в англ раскладке)
    dict = 0 #1-только англ слова, 2-только рус слова, 3-оба
    timer = 0 #таймер вывода "done!" на экран

    #массивы кнопок для ввода количества и длины
    number_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_KP0]

    #создание кнопок
    up = 140 #высота первой кнопки настроек
    dist = 70 #расстояние между кнопками
    settings_button = button_class(30, 30, 428, 45, "", "buttons/settings.png", "buttons/settings_hover.png")
    back_button = button_class(904, 30, 90, 45, "", "buttons/back.png", "buttons/back_hover.png")
    n_button = button_class(30, up, 460, 45, "", "buttons/n.png", "buttons/n_hover.png")
    n_minus_button = button_class(668, up, 90, 51, "", "buttons/minus.png", "buttons/minus_hover.png")
    n_enter_button = button_class(768, up, 126, 51, "", "buttons/enter.png", "buttons/enter_hover.png")
    n_plus_button = button_class(904, up, 90, 51, "", "buttons/plus.png", "buttons/plus_hover.png")
    length_button = button_class(30, up+dist, 231, 45, "", "buttons/length.png", "buttons/length_hover.png")
    length_minus_button = button_class(668, up+dist, 90, 51, "", "buttons/minus.png", "buttons/minus_hover.png")
    length_enter_button = button_class(768, up+dist, 126, 51, "", "buttons/enter.png", "buttons/enter_hover.png")
    length_plus_button = button_class(904, up+dist, 90, 51, "", "buttons/plus.png", "buttons/plus_hover.png")
    letters_button = button_class(30, up+dist*2, 231, 45, "", "buttons/letters.png", "buttons/letters_hover.png")
    letters_no_button = button_class(642, up+dist*2, 171, 51, "", "buttons/no.png", "buttons/no_hover.png")
    letters_no_select_button = button_class(642, up + dist * 2, 171, 51, "", "buttons/no_select.png", "buttons/no_select_hover.png")
    letters_yes_button = button_class(823, up+dist*2, 171, 51, "", "buttons/yes.png", "buttons/yes_hover.png")
    letters_yes_select_button = button_class(823, up + dist * 2, 171, 51, "", "buttons/yes_select.png", "buttons/yes_select_hover.png")
    register_button = button_class(30, up+dist*3, 310, 45, "", "buttons/register.png", "buttons/register_hover.png")
    register_button_off = button_class(30, up+dist*3, 310, 45, "", "buttons/register_hover.png", "buttons/register_hover.png")
    register_down_button = button_class(642, up+dist*3, 171, 51, "", "buttons/down.png", "buttons/down_hover.png")
    register_down_select_button = button_class(642, up + dist * 3, 171, 51, "", "buttons/down_select.png", "buttons/down_select_hover.png")
    register_down_button_off = button_class(642, up+dist*3, 171, 51, "", "buttons/down_hover.png", "buttons/down_hover.png")
    register_up_button = button_class(823, up+dist*3, 171, 51, "", "buttons/up.png", "buttons/up_hover.png")
    register_up_select_button = button_class(823, up + dist * 3, 171, 51, "", "buttons/up_select.png", "buttons/up_select_hover.png")
    register_up_button_off = button_class(823, up+dist*3, 171, 51, "", "buttons/up_hover.png", "buttons/up_hover.png")
    numbers_button = button_class(30, up+dist*4, 231, 45, "", "buttons/numbers.png", "buttons/numbers_hover.png")
    numbers_no_button = button_class(642, up + dist * 4, 171, 51, "", "buttons/no.png", "buttons/no_hover.png")
    numbers_no_select_button = button_class(642, up + dist * 4, 171, 51, "", "buttons/no_select.png","buttons/no_select_hover.png")
    numbers_yes_button = button_class(823, up + dist * 4, 171, 51, "", "buttons/yes.png", "buttons/yes_hover.png")
    numbers_yes_select_button = button_class(823, up + dist * 4, 171, 51, "", "buttons/yes_select.png","buttons/yes_select_hover.png")
    replaces_button = button_class(30, up+dist*5, 290, 45, "", "buttons/replaces.png", "buttons/replaces_hover.png")
    replaces_button_off = button_class(30, up + dist * 5, 290, 45, "", "buttons/replaces_hover.png", "buttons/replaces_hover.png")
    replaces_no_button = button_class(642, up + dist * 5, 171, 51, "", "buttons/no.png", "buttons/no_hover.png")
    replaces_no_select_button = button_class(642, up + dist * 5, 171, 51, "", "buttons/no_select.png","buttons/no_select_hover.png")
    replaces_no_button_off = button_class(642, up + dist * 5, 171, 51, "", "buttons/no_hover.png", "buttons/no_hover.png")
    replaces_yes_button = button_class(823, up + dist * 5, 171, 51, "", "buttons/yes.png", "buttons/yes_hover.png")
    replaces_yes_select_button = button_class(823, up + dist * 5, 171, 51, "", "buttons/yes_select.png", "buttons/yes_select_hover.png")
    replaces_yes_button_off = button_class(823, up + dist * 5, 171, 51, "", "buttons/yes_hover.png", "buttons/yes_hover.png")
    specials_button = button_class(30, up+dist*6, 573, 45, "", "buttons/specials.png", "buttons/specials_hover.png")
    specials_no_button = button_class(642, up + dist * 6, 171, 51, "", "buttons/no.png", "buttons/no_hover.png")
    specials_no_select_button = button_class(642, up + dist * 6, 171, 51, "", "buttons/no_select.png","buttons/no_select_hover.png")
    specials_yes_button = button_class(823, up + dist * 6, 171, 51, "", "buttons/yes.png", "buttons/yes_hover.png")
    specials_yes_select_button = button_class(823, up + dist * 6, 171, 51, "", "buttons/yes_select.png", "buttons/yes_select_hover.png")
    dict_button = button_class(30, up+dist*7, 235, 45, "", "buttons/dict.png", "buttons/dict_hover.png")
    dict_no_button = button_class(461, up + dist * 7, 171, 51, "", "buttons/no.png", "buttons/no_hover.png")
    dict_no_select_button = button_class(461, up + dist * 7, 171, 51, "", "buttons/no_select.png", "buttons/no_select_hover.png")
    dict_eng_button = button_class(642, up + dist * 7, 171, 51, "", "buttons/eng.png", "buttons/eng_hover.png")
    dict_eng_select_button = button_class(642, up + dist * 7, 171, 51, "", "buttons/eng_select.png", "buttons/eng_select_hover.png")
    dict_ru_button = button_class(823, up + dist * 7, 171, 51, "", "buttons/ru.png", "buttons/ru_hover.png")
    dict_ru_select_button = button_class(823, up + dist * 7, 171, 51, "", "buttons/ru_select.png", "buttons/ru_select_hover.png")
    generate_off_button = button_class(30, up+dist*8, 582, 45, "", "buttons/generate_off.png", "buttons/generate_off.png")
    generate_on_button = button_class(30, up + dist * 8, 582, 45, "", "buttons/generate_on.png", "buttons/generate_hover.png")
    done_button = button_class(622, up + dist * 8, 355, 45, "", "buttons/done.png", "buttons/done.png")

    #массив кнопок для постоянного вывода
    buttons_list = [settings_button, back_button, n_button, n_minus_button, n_enter_button,
                    n_plus_button, length_button, length_minus_button, length_enter_button, length_plus_button,
                    letters_button, letters_no_button, letters_yes_select_button, register_button_off, register_down_button_off,
                    register_up_button_off, numbers_button, numbers_no_button, numbers_yes_select_button, replaces_button,
                    replaces_no_button, replaces_yes_select_button, specials_button, specials_no_button, specials_yes_select_button,
                    generate_off_button, dict_button, dict_no_select_button, dict_eng_button, dict_ru_button]

    #кнопки непостоянного вывода и индикатор их вывода
    n_input_button = button_class (768, up, 126, 51, "", "buttons/input.png", "buttons/input.png")
    n_input = False
    length_input_button = button_class (768, up+dist, 126, 51, "", "buttons/input.png", "buttons/input.png")
    length_input = False

    running = True
    while running:
        # вывод фон
        screen.fill((0, 0, 0))
        screen.blit(background_settings, (0, 0))

        #вывод текста
        font = pygame.font.Font('fonts/Trigram.ttf', 40)
        text_surface_n = font.render(n, True, (85, 156, 173))
        text_rect_n = text_surface_n.get_rect(center=(831, 25+up))
        screen.blit(text_surface_n, text_rect_n)
        text_surface_length = font.render(length, True, (85, 156, 173))
        text_rect_length = text_surface_length.get_rect(center=(831, 25+up+dist))
        screen.blit(text_surface_length, text_rect_length)

        #вывод кнопок
        for buttons in buttons_list:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        #кнопка ввода количества
        if n_input:
            if int(time.time()) % 2 == 0:
                n_input_button.draw(screen)

        #кнопка ввода длины
        if length_input:
            if int(time.time()) % 2 == 0:
                length_input_button.draw(screen)

        #кнопки параметра букв
        if letters:
            buttons_list[11] = letters_no_button
            buttons_list[12] = letters_yes_select_button
            buttons_list[13] = register_button
            buttons_list[14] = register_down_button
            buttons_list[15] = register_up_button

        if not letters:
            register = 0
            register_up = False
            register_down = False
            buttons_list[11] = letters_no_select_button
            buttons_list[12] = letters_yes_button
            buttons_list[13] = register_button_off
            buttons_list[14] = register_down_button_off
            buttons_list[15] = register_up_button_off

        #кнопки параметра регистра
        if register_down:
            buttons_list[14] = register_down_select_button
        if not register_down and letters:
            buttons_list[14] = register_down_button
        if register_up:
            buttons_list[15] = register_up_select_button
        if not register_up and letters:
            buttons_list[15] = register_up_button

        #кнопки параметра цифр
        if numbers:
            buttons_list[17] = numbers_no_button
            buttons_list[18] = numbers_yes_select_button
        if not numbers:
            buttons_list[17] = numbers_no_select_button
            buttons_list[18] = numbers_yes_button

        #кнопки параметра замен
        if (not (numbers and letters)) and (not dict_eng) and (not dict_ru):
            replaces = False
            buttons_list[19] = replaces_button_off
            buttons_list[20] = replaces_no_button_off
            buttons_list[21] = replaces_yes_button_off
        if replaces:
            buttons_list[19] = replaces_button
            buttons_list[20] = replaces_no_button
            buttons_list[21] = replaces_yes_select_button
        if (not replaces) and ((numbers and letters) or dict_eng or dict_ru):
            buttons_list[19] = replaces_button
            buttons_list[20] = replaces_no_select_button
            buttons_list[21] = replaces_yes_button

        #кнопки параметра спец символов
        if specials:
            buttons_list[23] = specials_no_button
            buttons_list[24] = specials_yes_select_button
        if not specials:
            buttons_list[23] = specials_no_select_button
            buttons_list[24] = specials_yes_button

        #кнопки параметра слов
        if dict_eng:
            buttons_list[27] = dict_no_button
            buttons_list[28] = dict_eng_select_button
        else:
            buttons_list[28] = dict_eng_button
        if dict_ru:
            buttons_list[27] = dict_no_button
            buttons_list[29] = dict_ru_select_button
        else:
            buttons_list[29] = dict_ru_button
        if (not dict_eng) and (not dict_ru):
            buttons_list[27] = dict_no_select_button
            buttons_list[28] = dict_eng_button
            buttons_list[29] = dict_ru_button

        #кнопка генерации паролей
        if (not letters) and (not numbers) and (not specials) and (not dict_eng) and (not dict_ru):
            buttons_list[25] = generate_off_button
        elif letters and (not register_down) and (not register_up):
            buttons_list[25] = generate_off_button
        else:
            buttons_list[25] = generate_on_button

        #таймер вывода "done"
        if (time.time()) < timer:
            done_button.draw(screen)

        #действия
        for event in pygame.event.get():
            #кнопки
            for buttons in buttons_list:
                buttons.handle_event(event)

            #выход
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            #ввод количества (ограничен цифрами)
            if n_input:
                if event.type == pygame.KEYDOWN and len(event.unicode) != 0:
                    if 47 < ord(event.unicode) < 58:
                        n += event.unicode
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    n = n[:-1]
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    n_input = False
                    if len(n) == 0:
                        n = "1"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    n_input = False
                    if len(n) == 0:
                        n = "1"

            #ввод длины (ограничен цифрами)
            if length_input:
                if event.type == pygame.KEYDOWN and len(event.unicode) != 0:
                    if 47 < ord(event.unicode) < 58:
                        length += event.unicode
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    length = length[:-1]
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    length_input = False
                    if len(length) == 0:
                        length = "1"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    length_input = False
                    if len(length) == 0:
                        length = "1"

            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()

            if event.type == pygame.USEREVENT and event.button == n_minus_button:
                if int(n) > 1:
                    n = str(int(n) - 1)
            if event.type == pygame.USEREVENT and event.button == n_enter_button:
                n_input = True
            if event.type == pygame.USEREVENT and event.button == n_plus_button:
                n = str(int(n) + 1)

            if event.type == pygame.USEREVENT and event.button == length_minus_button:
                if int(length) > 1:
                    length = str(int(length) - 1)
            if event.type == pygame.USEREVENT and event.button == length_enter_button:
                length_input = True
            if event.type == pygame.USEREVENT and event.button == length_plus_button:
                length = str(int(length) + 1)

            if event.type == pygame.USEREVENT and event.button == letters_yes_button:
                letters = True
            if event.type == pygame.USEREVENT and event.button == letters_no_button:
                letters = False

            if event.type == pygame.USEREVENT and event.button == register_down_button:
                register_down = True
            if event.type == pygame.USEREVENT and event.button == register_down_select_button:
                register_down = False
            if event.type == pygame.USEREVENT and event.button == register_up_button:
                register_up = True
            if event.type == pygame.USEREVENT and event.button == register_up_select_button:
                register_up = False

            if event.type == pygame.USEREVENT and event.button == numbers_yes_button:
                numbers = True
            if event.type == pygame.USEREVENT and event.button == numbers_no_button:
                numbers = False

            if event.type == pygame.USEREVENT and event.button == replaces_yes_button:
                replaces = True
            if event.type == pygame.USEREVENT and event.button == replaces_no_button:
                replaces = False

            if event.type == pygame.USEREVENT and event.button == specials_yes_button:
                specials = True
            if event.type == pygame.USEREVENT and event.button == specials_no_button:
                specials = False

            if event.type == pygame.USEREVENT and event.button == dict_no_button:
                dict_eng = False
                dict_ru = False
            if event.type == pygame.USEREVENT and event.button == dict_eng_button:
                dict_eng = True
            if event.type == pygame.USEREVENT and event.button == dict_ru_button:
                dict_ru = True
            if event.type == pygame.USEREVENT and event.button == dict_eng_select_button:
                dict_eng = False
            if event.type == pygame.USEREVENT and event.button == dict_ru_select_button:
                dict_ru = False

            if event.type == pygame.USEREVENT and event.button == generate_on_button:
                if register_up:
                    register += 1
                if register_down:
                    register += 2
                if dict_eng:
                    dict += 1
                if dict_ru:
                    dict += 2
                generate_passwords(int(n), int(length), letters, register, numbers, replaces, specials, dict)
                timer = int(time.time()) + 2
                register = 0
                dict = 0

        pygame.display.flip()


#вызов функции главного меню, включение
main_menu()