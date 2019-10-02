import socket
  
s = socket.socket()   
s.connect(('headnode', 5000))
mensaje = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','quit']
while True:
  if (len(mensaje)==0):
    break
  
  
  s.sendall(mensaje[0].encode())

  mensaje.pop(0)
  recibido = bytes.decode(s.recv(1024))
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
print("Cerrando Cliente")  
  

