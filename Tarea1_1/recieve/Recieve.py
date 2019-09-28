import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('server', 5000))
s.listen(9)
conn, addr = s.accept()
print("accepted")
print(bytes.decode(conn.recv(1024)))

print ("hello")
