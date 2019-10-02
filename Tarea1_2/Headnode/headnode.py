import socket
from random import randint

ser_cli = socket.socket()   
ser_cli.bind(('headnode', 5000)) 
ser_dat1 = socket.socket()   
ser_dat1.bind(('headnode', 5001))
ser_dat2 = socket.socket()   
ser_dat2.bind(('headnode', 5002)) 
ser_dat3 = socket.socket()   
ser_dat3.bind(('headnode', 5003))  
ser_cli.listen(1) 
ser_dat1.listen(1)
ser_dat2.listen(1)
ser_dat3.listen(1)
sc, addr = ser_cli.accept()
sd1, addr1 = ser_dat1.accept()
sd2, addr2 = ser_dat2.accept() 
sd3, addr3 = ser_dat3.accept()  
while True:
  list_recib=['recibido1','recibido2','recibido3']
  recibido = bytes.decode(sc.recv(1024))
  if recibido == "quit":
    recibido1 = "saliendo"

    sd1.sendall(str(recibido).encode())
    sd2.sendall(str(recibido).encode())
    sd3.sendall(str(recibido).encode())
    sc.sendall(recibido1.encode())
    break        
  azar=randint(1,3)
  if (azar==1):
    sd1.sendall(str(recibido).encode())
    recibido1 = bytes.decode(sd1.recv(1024))
    if (recibido1=="guardado!"):
      servidor1="guardado en datanode 1 "
      sc.send(str(servidor1).encode())
  elif (azar==2):
    sd2.sendall(str(recibido).encode())
    recibido2 = bytes.decode(sd2.recv(1024))
    if (recibido2=="guardado!"):
      servidor2="guardado en datanode 2 "
      sc.send(str(servidor2).encode())

  elif (azar==3):
    sd3.sendall(str(recibido).encode())
    recibido3 = bytes.decode(sd3.recv(1024))
    if (recibido3=="guardado!"):
      servidor3="guardado en datanode 3 "
      sc.send(str(servidor3).encode())
  file = open("registro_server.txt","a")
  file.write("Se guardó el mensaje: " + recibido + ", en el datanode:"+str(azar)+"\n")
  file.close()

    
  
  #sc.sendall(recibido.encode())   

print("Cerrando Headnode") 

sc.close()  
ser_cli.close() 
sd1.close()
sd2.close()
sd3.close() 
