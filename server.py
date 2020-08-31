import socket
import thread
def handle(client_socket, address):
 while True:
  data = client_socket.recv(512)
  if data.startswith("exit"): # if data start with "exit"
   client_socket.close() # close the connection with the client
   break
  client_socket.send(data) # echo the received string
# opening the port 1075
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',16000))
server.listen(2)
while True: # listen for incoming connections
 client_socket, address = server.accept()
 print "request from the ip",address[0]
 # spawn a new thread that run the function handle()
 thread.start_new_thread(handle, (client_socket, address)) 