
import os
from utils import getKey
from race  import Race
from termcolor import colored


class Menu(object):


    def change_menu(self, choice, new_menu):
        key = getKey()
        if key == choice:
            new_menu()
            self.clean_screen()


    def welcome_menu(self):
        print("Welcome to Keyboard Race !")
        print("1. Solo \n2. Multiplayer")
        self.change_menu("1", self.game_screen)


    def game_screen(self):
        race = Race("Ceci est un test.")
        print(race.final_text)
        race.actual_text = "Ceci est"
        print(race.color_typed_text())
        print("GAME SCREEN")
        getKey()

    def solo_score_menu(self):
        raise NotImplementedError

    def multi_score_menu(self):
        raise NotImplementedError

    def print_porcentage(final_text, actual_text):
        return (len(actual_text) / len(final_text)) * 100

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def main_game_menu(self):
        self.welcome_menu()