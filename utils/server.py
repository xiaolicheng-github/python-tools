import socket

def get_ipv4_address():
    return socket.gethostbyname(socket.gethostname())

