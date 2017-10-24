import termios

import sys

import os
import tty

import termcolor

import requests

__fd = sys.stdin.fileno()
__old = termios.tcgetattr(__fd)


def __getKey():
    """Return a key pressed with ord"""
    try:
        tty.setcbreak(sys.stdin.fileno())
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        ch = sys.stdin.read(1)
        return ord(ch) if ch else None
    finally:
        termios.tcsetattr(__fd, termios.TCSADRAIN, __old)


def get_random_text():
    # TODO : Replace with a real random text
    return requests.get(
        "http://api.icndb.com/jokes/random").json()["value"]["joke"]


def getKey():
    """
    Key pressed as str
    :return:
    """
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    key = None
    try:
        key = os.read(fd, 3)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return key.decode()


def get_input_and_print_actual_text(race, color, key=None):
    if not key:
        key = getKey()
    race.check_key_pressed(key_pressed=key)
    clean_screen()
    print(
        color_typed_text(
            final_text=race.final_text,
            actual_text=race.actual_text,
            color=color))


# Colores the typed text in red and the rest in black
def color_typed_text(final_text, actual_text, color="red"):
    if actual_text:
        tmp = final_text.split(actual_text)
        return termcolor.colored(actual_text, color) + tmp[1]
    else:
        return final_text

# TODO: Save scores


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
