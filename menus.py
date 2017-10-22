
import os

import time

import utils
from race  import Race
import sys


# def change_menu(choice, new_menu):
#     key = utils.getKey()
#     if key == choice:
#         clean_screen()
#         new_menu()


def change_menu(choices_dict):
    key = utils.getKey()
    menu = choices_dict.get(key)
    if menu:
        clean_screen()
        menu()




def welcome_menu():
    print("Welcome to Keyboard Race !")
    print("1. Solo \n2. Multiplayer")
    change_menu({"1": solo_game, "2": multi_main_menu})


def get_key_and_print(race):
    first_stroke = utils.getKey()
    race.check_key_pressed(key_pressed=first_stroke)
    clean_screen()
    print(utils.color_typed_text(final_text=race.final_text, actual_text=race.actual_text))


def solo_game():
    race = Race(utils.get_random_text())
    print(race.final_text, "\nPress a key to begin...")
    get_key_and_print(race)
    race.start_time = time.time()
    while True:
        if race.check_if_win():
            print("You won !")
            show_statistics(race.get_statistics())
            print("""
            Press 'r' for restart a game
            Press 'm' for main menu
            Press 'q' for quit""")

            change_menu({"r" : solo_game, "m": welcome_menu, "q": leave})

            break


        get_key_and_print(race)


def multi_main_menu():
    pass


def leave():
    sys.exit()

def solo_score_menu():
    """
        Screen displayed at the end of a race in solo mode.
    """
    raise NotImplementedError

def multi_score_menu():
    """
        Screen displayed at the end of a multiplayer race.
    :return:
    """
    raise NotImplementedError

def print_porcentage(final_text, actual_text):
    return (len(actual_text) / len(final_text)) * 100

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_statistics(statistics):
    print("""
                Statistics
                ----------
                Speed : {0} char/s
                Wrongs :{1}
                Time : {2} seconds""".format(statistics.get("speed"), statistics.get("wrongs"), statistics.get("time")))

def main_game_menu():
    welcome_menu()