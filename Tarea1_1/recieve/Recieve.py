import socket
from datetime import datetime


s = socket.socket()   
s.bind(('server', 5000))  
s.listen(1)  

while True:

  sc, addr = s.accept()
  recibido = bytes.decode(sc.recv(1024))
  hora = datetime.now()
  horita = hora.strftime("%d/%m/%Y %H:%M:%S")
  file = open("log.txt","a")
  file.write("[" + horita + "] Se recivio el mensaje: " + recibido + ", desde la ip: " + addr[0] +"\n")
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
