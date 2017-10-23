import socket
import utils
from race import Race


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
    my_race = None
    opponent_race = None
    compteur = 0  # To check if it's the first connection or not

    host = "127.0.0.1"
    port = 5001

    server = ("127.0.0.1", 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    while True:
        print("1")
        if compteur == 0: #If this is the first connection
            s.sendto("new_connection".encode(), server)
            data, addr = s.recvfrom(1024)
            text = str(data.decode())
            race = Race(text)
            print("First connection. Text received :" + text)

        print("2")
        #data, addr = s.recvfrom(1024)
        print("3")
        message = utils.getKey()
        print("4")

        if message == "exit":
            s.sendto(message.encode(), server)
            # Dont' wait for answer
            break

        s.sendto(message.encode(), server)
        print("5")
        compteur += 1
        print("6")

    s.close()


if __name__ == "__main__":
    race_opponent()