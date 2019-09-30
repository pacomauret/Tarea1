import socket
 
s = socket.socket()   
s.bind(('127.0.0.1', 5000))  
s.listen(1)  

while True:

  sc, addr = s.accept()
  recibido = bytes.decode(sc.recv(1024))
  file = open("log.txt","w+")
  file.write("Se recivio el mensaje: " + recibido + ", desde la ip: " + addr[0] +"\n")
  file.close()
 
  if recibido == "quit":
    recibido = "saliendo"
    sc.sendall(recibido.encode())
    break          
  recibido = "recibido"
  sc.sendall(recibido.encode())  

print("adios") 

sc.close()  
s.close()  
