import termios

import sys

import os
import tty

import termcolor

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
    #TODO : Replace with a real random text
    return "Ceci est un test !"




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



# Colores the typed text in red and the rest in black
def color_typed_text(final_text, actual_text):
    if actual_text:
        tmp = final_text.split(actual_text)
        return termcolor.colored(actual_text, "red") + tmp[1]
    else:
        return final_text

#TODO: Save scores