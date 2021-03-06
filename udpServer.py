import socket

import time

import os

import menus
from race import Race
import utils

import threading


def chat():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM for udp
    s.bind((host, port))

    print("Starting server ...")
    while True:
        data, addr = s.recvfrom(1024)

        if str(data.decode()) == 'exit':
            break

        print("Message from {0}".format(str(addr)))
        print("Content : {0}".format(str(data.decode())))
        data = str(data.decode()).upper().encode()
        print("Sending after treatment...")
        s.sendto(data, addr)

    s.close()


def race_opponent():

    TEXT = "Ceci est le texte de course."
    my_race = Race(TEXT)
    opponent_race = Race(TEXT)
    compteur = 0  # To check if it's the first connection or not

    # Host screen for race
    host = "127.0.0.1"
    port = 5000
    addr = None

    finished = False

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM for udp
    s.bind((host, port))

    class MyThread(threading.Thread):

        def receive(self):
            threading.Timer(5, self.receive).start()
            data, addr = s.recvfrom(1024)
            if len(data.decode()) > 0:
                opponent_race.actual_text = str(data.decode())

        def __init__(self, event):
            threading.Thread.__init__(self)
            self.stopped = event

        def run(self):
            while not self.stopped.wait(1):
                    self.receive()
                    stopFlag.set()

    stopFlag = threading.Event()
    thread = MyThread(stopFlag)
    thread.start()

    print("Waiting for your opponent ...\n")
    while True:

        if compteur == 0:
            data, addr = s.recvfrom(1024)  # Receive the opponents informations
            print("Player found ! Game will begin in 5 seconds ...")
            print("Text : \n{0}".format(TEXT))
            s.sendto(TEXT.encode(), addr)
            time.sleep(3)
            menus.clean_screen()
            my_race.start_race()
            print("GO !")

        else:
            if my_race.check_if_finished():
                menus.clean_screen()
                print("YOU WON !")
                menus.show_statistics(my_race.get_statistics())
                stopFlag.set()
                finished = True
                break

            if opponent_race.check_if_finished():
                stopFlag.set()
                menus.clean_screen()
                print("YOU LOSE !")
                menus.show_statistics(my_race.get_statistics())
                finished = True
                break

            if not finished:
                print("Not finished")
                key = utils.getKey()
                menus.clean_screen()
                utils.get_input_and_print_actual_text(
                    key=key, race=my_race, color="green")
                s.sendto(my_race.actual_text.encode(), addr)
                utils.check_input_and_print_actual_text(
                    opponent_race.actual_text, opponent_race)

        compteur += 1
    s.close()
    print("Connection ended")


if __name__ == "__main__":
    race_opponent()
