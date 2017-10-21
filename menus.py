
import os

def welcome_menu():
    raise NotImplementedError

def solo_score_menu():
    raise NotImplementedError

def multi_score_menu():
    raise NotImplementedError

def print_porcentage(final_text, actual_text):
    return (len(actual_text) / len(final_text)) * 100

def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')