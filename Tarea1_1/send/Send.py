import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('0.0.0.0',5000))
command = "bridge test!"
adress= ('recieve',5000)
sock.connect(('server', 5000))
#x=sock.connect(adress)
#print("this is x=",x)
sock.sendall(command.encode())
sock.close()
