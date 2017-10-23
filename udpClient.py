import socket

def main():
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

if __name__ == "__main__":
    main()