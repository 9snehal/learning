import os
import signal
import socket
import time

SERVER_ADDRESS = (HOST,PORT) = '0.0.0.0',8888
REQUEST_QUEUE_SIZE = 5

def grim_reaper(signum,frame):
    pid,status = os.wait()
    print(
        'Child {pid} terminated with status {status}'
        '\n'.format(pid=pid, status=status)
    )

def handle_request(client_conn):
    request = client_conn.recv(1024)
    print(request.decode())
    http_response = """\
    HTTP/1.1 200 OK
    Hello, World
    """
    client_conn.sendall(http_response)
    time.sleep(3) 

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port}'.format(port=PORT))  

    signal.signal(signal.SIGCHLD, grim_reaper) 

    while True:
        client_conn,client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0 :
            listen_socket.close()
            handle_request(client_conn)
            client_conn.close()
            os._exit(0)
        else:
            client_conn.close()     


if __name__ == '__main__':
    serve_forever()
