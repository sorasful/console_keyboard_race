import os

import time

import utils
from race import Race
import sys
import udpServer
import udpClient


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



def solo_game():
    race = Race(utils.get_random_text())
    print(race.final_text, "\nPress a key to begin...")
    utils.get_input_and_print_actual_text(race)
    race.start_race()
    while True:
        if race.check_if_game_is_won():
            print("You won !")
            show_statistics(race.get_statistics())
            print("""
            Press 'r' for restart a game
            Press 'm' for main menu
            Press 'q' for quit""")

            change_menu({"r": solo_game, "m": welcome_menu, "q": leave})
            break

        utils.get_input_and_print_actual_text(race)


def multi_main_menu():
    print("""
    1. Host
    2. Join a server""")

    change_menu({"1": host_screen, "2": join_screen })


def host_screen():
    udpServer.race_opponent()

def join_screen():
    server_ip = input("Enter server ip: (This is not used yet) ")
    udpClient.race_opponent()

def leave():
    sys.exit()


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
