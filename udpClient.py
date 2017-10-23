import socket

import time

import os

import menus
import utils
from race import Race

import threading


def chat():
    host = "127.0.0.1"
    port = 5001

    server = ("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    while True:
        message = input("-> ")
        if message == "exit":
            s.sendto(message.encode(), server)
            # Dont' wait for answer
            break

        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("Received message from {0} : {1}".format(str(addr), str(data.decode())))

    s.close()


def race_opponent():
    text = ""
    my_race = Race(text)
    opponent_race = Race(text)
    compteur = 0  # To check if it's the first connection or not

    host = "127.0.0.1"
    port = 5001 # Must be different from server
    addr = None

    server = ("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    while True:

        class MyThread(threading.Thread):

            def receive(self):
                threading.Timer(1, self.receive).start()
                data, addr = s.recvfrom(1024)
                if len(data) > 0:
                    opponent_race.actual_text = str(data.decode())

            def __init__(self, event):
                threading.Thread.__init__(self)
                self.stopped = event

            def run(self):
                while not self.stopped.wait(1):
                    self.receive()
                    # call a function

                    time.sleep(20)
                    stopFlag.set()

        stopFlag = threading.Event()
        thread = MyThread(stopFlag)
        thread.start()

        if compteur == 0: #If this is the first connection
            s.sendto("new_connection".encode(), server)
            data, addr = s.recvfrom(1024)
            text = str(data.decode())
            print("Connection successful ! Game will begin in 5 seconds.")
            print("Text : \n{0}".format(text))
            my_race = Race(text)
            opponent_race = Race(text)
            time.sleep(5)
            menus.clean_screen()
            my_race.start_time = time.time()
            opponent_race.start_time = time.time()
            print("GO !")


        else:

            if my_race.check_if_game_is_won():
                menus.clean_screen()
                print("YOU WON !")
                menus.show_statistics(my_race.get_statistics())
                break

            if opponent_race.check_if_game_is_won():
                menus.clean_screen()
                print("YOU LOSE !")
                menus.show_statistics(my_race.get_statistics())
                break

            key = utils.getKey()
            menus.clean_screen()
            utils.get_input_and_print_actual_text(key=key, race=my_race, color="green")
            s.sendto(my_race.actual_text.encode(), server)
            utils.check_input_and_print_actual_text(opponent_race.actual_text, opponent_race)


        compteur += 1

    s.close()


if __name__ == "__main__":
    race_opponent()