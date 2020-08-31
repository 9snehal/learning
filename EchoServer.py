# Echo server program
import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 15001             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

conn, addr = s.accept()
print 'Connected by', addr
while 1:
  print 'trying to receive data'
  data = conn.recv(1024)
  print 'data receive'
  if not data: break
  conn.sendall(data)
conn.close()