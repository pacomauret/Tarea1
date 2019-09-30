import socket


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('server', 5000))
#s.listen(9)
#conn, addr = s.accept()
#print("accepted")
#print(bytes.decode(conn.recv(1024)))

#print ("hello")
 
s = socket.socket()   
s.bind(('server', 5000))  
s.listen(1)  

sc, addr = s.accept()  

while True:  
  recibido = bytes.decode(sc.recv(1024))  
  if recibido == "quit":
     print("Recibido:", recibido)  
     break        
  print("Recibido:", recibido)  
  sc.send(recibido.encode())  

print("adios") 

sc.close()  
s.close()  
