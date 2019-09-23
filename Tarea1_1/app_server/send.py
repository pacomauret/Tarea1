import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
command = "bridge test!"
x=sock.connect(('172.17.0.1', 5000))
print("this is x=",x)
sock.sendall(command.encode())
