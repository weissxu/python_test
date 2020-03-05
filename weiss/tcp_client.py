from socket import socket

s = socket()
s.connect(('localhost', 9999))
print(s.recv(1024).decode('utf-8'))

for data in [b'micheal', b'tray', b'slash']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
