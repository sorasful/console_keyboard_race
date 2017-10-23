import socket
import menus
from race import Race
import utils

def chat():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #DGRAM for udp
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

    compteur = 0 # To check if it's the first connection or not

    # Host screen for race
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM for udp
    s.bind((host, port))

    print("Waiting for your opponent ...\n")
    while True:
        print("1")
        data, addr = s.recvfrom(1024)
        str_data = data.decode()
        print("2")
        # Client is connected
        # We send the text to the client
        if str_data == "new_connection": # If this is the first connection:
            print("3")
            s.sendto(TEXT.encode(), addr)
            print("4")

        else:
            print("5")
            utils.get_input_and_print_actual_text(my_race, color="green")

            utils.check_input_and_print_actual_text(str_data, opponent_race)
            print("6")

            # print("{0}\t -> Me".format(utils.color_typed_text(final_text=my_race.final_text, actual_text=my_race.actual_text,
            #                                                   color="green")))
            # print("{0}\t -> Opponent".format(utils.color_typed_text(final_text=opponent_race.final_text,
            #                                                         actual_text=opponent_race.actual_text)))
        # menus.clean_screen()

        if str(data.decode()) == 'exit':
            break

        compteur += 1
        print("7")


            # data = str(data.decode()).upper().encode()
        # print("Sending after treatment...")
        # s.sendto(data, addr)

    s.close()


if __name__ == "__main__":
    # chat()
    race_opponent()