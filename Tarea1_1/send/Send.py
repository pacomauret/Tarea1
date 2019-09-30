import socket
  
s = socket.socket()   
s.connect(('127.0.0.1', 5000))
  
while True:

  mensaje = "quit"
  s.sendall(mensaje.encode())

  recibido = bytes.decode(s.recv(1024))

  file = open("respuesta.txt","w+")
  file.write("Se recivio la respuesta: " + recibido + ", desde el servidor\n")
  file.close()
   
  if recibido == "saliendo": 
    break  
  
print("adios")  
  
s.close()
