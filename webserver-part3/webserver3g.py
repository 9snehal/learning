import errno
import os
import signal
import socket

SERVER_ADDRESS = (HOST,PORT)= '0.0.0.0',8888
REQUEST_QUEUE_SIZE = 1024

def grim_reaper(signum,frame):
    while True:
        try:
            pid,status = os.waitpid(
                -1,   # waiting for child process
                os.WNOHANG  # don't block and return EWOULDBLOCK error
            )
        except OSError:
            return

        if pid == 0:
            return


def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = """\
    HTTP/1.1 200 OK
    HELLO WORLD
    """

    client_connection.sendall(http_response)

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port}'.format(port=PORT))

    signal.signal(signal.SIGCHLD, grim_reaper)
    
    while True:
        try:
            client_connection,client_address = listen_socket.accept()
        except IOError as e:
            code,msg = e.args
            if code == errno.EINTR:
                continue
            else:
                raise

        pid = os.fork()

        if pid == 0:
            listen_socket.close()
            handle_request(client_connection)
            client_connection.close()
            os._exit(0)
        else:
            client_connection.close()


if __name__ == "__main__":
    serve_forever()