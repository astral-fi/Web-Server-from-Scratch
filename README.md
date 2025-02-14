Web Address : 

https://hostname:port/path 

TCP : Virtual Connection between two devices that allows them to exchange data over a network

Client and Server need to create a TCP Connection before it can send a HTTP Request. 
It is made using sockets. 

$telnet hostname port -> Help us create a TCP Connection with the local server.
$GET path http-version -> Help us make a HTTP Request and in return gets a response which is displayed on the browser/terminal.


The Web server creates a listening socket and starts accepting new connections in a loop. The client initiates a TCP connection and, after successfully establishing it, the client sends an HTTP request to the server and the server responds with an HTTP response that gets displayed to the user. To establish a TCP connection both clients and servers use sockets.

A Socket is an abstraction of a communication endpoint and it allows your program to communicate with another program using file descriptors. 

Ephemeral Port : A Dynamic port assigned by OS and is released after use.
Well-Known Ports: Reserved ports for system functions and wellknown services. 

A process is just an instance of an executing program. Every Process has ID assigned to it, a process had Process ID and Parent Process ID assigned to it. 
-> os.getpid() & os.getppid()

A file descriptor is a non-negative integer kernel returns to a process when it open an existing file, create a file or a new socket. 

The BACKLOG argument determines the size of a queue within the kernel for incoming connection requests. BACKLOG helps new connections to make connection but still the connections are dealt sequentially and hence would case delay.

Concurrent Servers deal with all the connections parallarly.
We use os.fork to do that. os.fork create a child process and then the child handles HTTP Request while Parents keep recieving new connect requets. 

WSGI(Web Server Gateway Interface) allowed developers to separate choice of a Web framework from choice of a Web Server.

