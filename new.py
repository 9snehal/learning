import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1234
s.setblocking(0)
print("start listening")
s.bind((host,port))
s.listen(5)
inputs=[s]
outputs=[]
while True:
    time.sleep(2)
    try:
        print "waiting for connection socket"
        conn, addr = s.accept()
        print(conn)
        print "socket connected"
        # print(addr)
        while True:
            time.sleep(2)
            try:
                print('Trying to read')
                data = conn.recv(1024) 
                conn.sendall(data)  
                print('got data') 
                print(data)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
conn.close()        

# import socketserver

# class MyTCPHandler(socketserver.BaseRequestHandler):
#     """
#     The request handler class for our server.

#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """

#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999

#     # Create the server, binding to localhost on port 9999
#     with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
#         # Activate the server; this will keep running until you
#         # interrupt the program with Ctrl-C
#         server.serve_forever()