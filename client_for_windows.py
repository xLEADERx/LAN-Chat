import socket
import select
import sys
from threading import Thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server.connect((IP_address, Port))


def inp(c, i):
    data = input()
    server.send(bytes(data, 'utf-8'))


def start100thread():
    for _ in range(60):
        t = Thread(target=inp, args=(1, 2))
        t.start()


while True:
    start100thread()
    print('here')
    message = server.recv(2048)
    print(message.decode())


server.close()

#myby working on windows but not working in linux (please check on windows)