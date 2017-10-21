#!/usr/bin/python3.5

from menus import Menu
from race import Race
import sys
import termios
import os

menu_instance = Menu()

def menu():
    menu_instance.main_game_menu()




def main():
    menu()

if __name__ == "__main__":
    main()