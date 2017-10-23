import socket

def main():
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

if __name__ == "__main__":
    main()
