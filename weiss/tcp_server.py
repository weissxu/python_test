import threading
import time
from socket import socket


def tcplink(sock, addr):
    print('accept new connection from %s:%s' % (sock, addr))
    sock.send(b'welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)

        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection closed')


s = socket()
s.bind(('localhost', 9999))
s.listen(5)
print('waiting for connections..')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
