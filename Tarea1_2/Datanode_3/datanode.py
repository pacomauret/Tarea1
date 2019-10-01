import socket
  
s = socket.socket()   
s.connect(('headnode', 5003))
  
while True:
  #mensaje = input("Enter Employee Name")
  #s.sendall(mensaje.encode())

  recibido = bytes.decode(s.recv(1024))
  print ("recibido =",recibido)
  if (recibido!="" and recibido !="quit"):
    file = open("data.txt","a")
    file.write("Se recibio el mensaje: " + recibido + ", desde el servidor\n")
    file.close()
  ok='guardado!'
  s.sendall(ok.encode())
  if (recibido=='quit'):
    break
  #if recibido == "saliendo": 
  #  break  
  
print("adios")  
  
s.close()
