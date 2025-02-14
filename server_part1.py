import socket
import time

HOST, PORT = '', 8888 

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket() -> creates a new socket object
#AF_INET -> specifies the address family, in this case, IPv4
#SOCK_STREAM -> specifies the socket type, in this case, sock stream which means it is TCP 

listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Helps the Server use the above address and port as soon as the server restarted

listen_socket.bind((HOST, PORT))
listen_socket.listen(5)

while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    reponse = b"""\
    HTTP/1.1 200 OK\n\nHello World! """
    client_connection.sendall(reponse)
    client_connection.close()

