
import os

import time

import utils
from race  import Race


def change_menu(choice, new_menu):
    key = utils.getKey()
    if key == choice:
        clean_screen()
        new_menu()



def welcome_menu():
    print("Welcome to Keyboard Race !")
    print("1. Solo \n2. Multiplayer")
    change_menu("1", solo_game)
    change_menu("2", multi_score_menu)


def solo_game():
    race = Race(utils.get_random_text())
    print(race.final_text, "\nPress a key to begin...")
    utils.getKey()
    clean_screen()
    race.start_time = time.time()
    while True:
        if race.check_if_win():
            print("You won !")
            break

        key = utils.getKey()
        race.check_key_pressed(key_pressed=key)
        clean_screen()
        print(utils.color_typed_text(final_text=race.final_text, actual_text=race.actual_text))



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



def main_game_menu():
    welcome_menu()