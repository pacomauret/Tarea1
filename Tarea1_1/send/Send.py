import socket
from datetime import datetime
 
s = socket.socket()   
s.connect(('server', 5000))
  
while True:

  mensaje = "quit"
  s.sendall(mensaje.encode())

  recibido = bytes.decode(s.recv(1024))

  hora = datetime.now()
  horita = hora.strftime("%d/%m/%Y %H:%M:%S")
  file = open("respuesta.txt","a")
  file.write("[" + horita + "] Se recivio la respuesta: " + recibido + ", desde el servidor\n")
  file.close()
   
  if recibido == "saliendo": 
    break  
  
print("adios")  
  
s.close()
