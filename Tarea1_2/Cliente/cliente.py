import socket
  
s = socket.socket()   
s.connect(('headnode', 5000))
while True:

  
  mensaje = input("Ingrese Datos: ")
  s.sendall(mensaje.encode())

  recibido = bytes.decode(s.recv(1024))
  print("recibido : ", recibido)
  try:
    servidor=str(recibido).split(" ")[3]
    file = open("data.txt","a")
    file.write("El mensaje se guardó en el datanode: " + servidor+"\n")
    file.close()
  except:
    x=':)'
  if recibido == "saliendo": 
    break  
  x=recibido
s.close()
print("adios")  
  

