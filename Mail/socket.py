#server

import socket
mysocket=socket.socket()
#to get the system name
#socket.gethostname()

#to get system ip
#socket.gethostbyname(socket.gethostname())

mysocket.bind((socket.gethostbyname(socket.gethostname())),8888)
mysocket.listen(2)
while True:
   conn,addr=mysocket.accept()
   msg='Got connection'
   conn.send(msg).encode()
   print('IP address of client',addr)
#client
import socket
mysocket=socket.socket()
mysocket.connect((socket.gethostbyname(socket.gethostname()),8888))
message=mysocket.recv(1024)
print(message.decode())
mysocket.close()