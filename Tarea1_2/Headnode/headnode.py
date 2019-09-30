import socket


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('server', 5000))
#s.listen(9)
#conn, addr = s.accept()
#print("accepted")
#print(bytes.decode(conn.recv(1024)))

#print ("hello")
 
s = socket.socket()   
s.bind(('headnode', 5000))  
s.listen(1)  

sc, addr = s.accept()  

while True:
	mensaje = "estado"
	sc.sendall(mensaje.encode())
	recibido = bytes.decode(sc.recv(1024))  
	if recibido == "ok":
		quit="quit" 
		sc.send(quit.encode())
		break        
	print("Recibido:", recibido)  
	sc.send(recibido.encode())  

print("adios") 

sc.close()  
s.close()  
