import os
import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
listen_socket.bind(('127.0.0.1', 8000))
listen_socket.listen(3)

while True:
    conn,addr = listen_socket.accept()

    pid = os.fork()

    if pid == 0: #child
        listen_socket.close()
        while True:
            data = conn.recv(1024)
            print data
            conn.sendall("[%s:%s]data" % (os.getpid(),os.getppid()))
            # conn.sendall("[%s:%s] data" % (os.getpid(), os.getppid()))
            conn.sendall(data)
            # conn.close()
    else:
        conn.close()        