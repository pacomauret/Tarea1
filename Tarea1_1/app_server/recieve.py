import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 5000))
s.listen(15)
conn, addr = s.accept()
print("accepted")
print(bytes.decode(conn.recv(1024)))