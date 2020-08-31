#!/usr/bin/python
import sys
import time
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
port = 60000
s.setblocking(0)
s.bind(("127.0.0.1" , port))

s.listen(10)
while 1:
    time.sleep(9)
    print "waiting for connection socket"
    conn, addr = s.accept()  
    print(conn)
    print "socket connected"
    while 1:
        time.sleep(2)
        print('Trying to read')
        msg = conn.recv(1024)
        conn.sendall(msg)  
        print('got data')
conn.close()

# import SocketServer

# class MyTCPHandler(SocketServer.BaseRequestHandler):
#     """
#     The RequestHandler class for our server.

#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """

#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         # print "{} wrote:".format(self.client_address[0])
#         print(self.data)
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())

# if __name__ == "__main__":
#     HOST, PORT = "127.0.0.1", 9999

#     # Create the server, binding to localhost on port 9999
#     server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

#     # Activate the server; this will keep running until you
#     # interrupt the program with Ctrl-C
#     server.serve_forever()