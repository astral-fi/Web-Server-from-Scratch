#Implementing Concurrent Servers 

import socket 
import os 

ADDR, PORT = '', 8888

def handle_request(client_connection):
    request = client_connection.recv(1024)
    print("CHILD PID {pid} ; PARENT PID {ppid}".format(
        pid = os.getpid(),
        ppid = os.getppid(),
    ))

    response = b"""\
HTTP/1.1 200 OK\n\nHello, World!! os.pid(), os.ppid(),
"""
    client_connection.sendall(response)


def server_create():
    listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen.bind((ADDR, PORT))
    listen.listen(5)

    while True:
        connection, address = listen.accept()
        pid = os.fork() #Creates a Child
        if pid == 0:
            listen.close()
            handle_request(connection)
            connection.close()
            os._exit(0)
        else:
            connection.close() #Closes Parent


if __name__ == '__main__':
    server_create()