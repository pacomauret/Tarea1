from random import randint
from threading import Thread 
from socketserver import ThreadingMixIn 
import socket
import time
import struct
import sys

class ClientThread(Thread): 

  def __init__(self,ip,port): 
    Thread.__init__(self) 
    self.ip = ip 
    self.port = port
    self.Datanodes = ["Datanode1","Datanode2","Datanode3"] 
    print("[+] New server socket thread started for " + ip + ":" + str(port)) 

  def run(self):
    while True:
      for i in range(1,6):
        print(i)
        time.sleep(1)
      message = 'Datanode return status'
      multicast_group = ('224.3.29.71', 5000)

      # Create the datagram socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

      # Set a timeout so the socket does not block
      # indefinitely when trying to receive data.
      sock.settimeout(1)

      # Set the time-to-live for messages to 1 so they do not
      # go past the local network segment.
      ttl = struct.pack('b', 1)
      sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
      Lista_status = ["caido","caido","caido"]

      try:

          # Send data to the multicast group
          print('enviando mensaje multicast... {!r}'.format(message))
          sent = sock.sendto(message.encode(), multicast_group)

          # Look for responses from all recipients
          while True:
              print('Esperando respuestas')
              try:
                  data, address = sock.recvfrom(16)
                  print(data)
                  if data == b'Datanode1':
                    Lista_status[0] = "activo"
                  elif data == b'Datanode2':
                    Lista_status[1] = "activo"
                  elif data == b'Datanode3':
                    Lista_status[2] = "activo"  
              except socket.timeout:
                  print('timed out')
                  break
              else:
                  print('received ',data)

          string = "Datanode 1: " + Lista_status[0] + " Datanode 2: " + Lista_status[1] + " Datanode 3: " + Lista_status[2] 

          file = open("hearbeat_server.txt","a")
          file.write("Nodes status: " + string + "\n")
          file.close()

      except socket.timeout:
          print("timed out")
  

#----------------------Multicast Thread---------------------------------
MCAST_GRP = '224.3.29.71'
MCAST_PORT = 5000
#Thread multicast se inicia en un principio para comenzar a pingear a los datanodes
Datanode1 = ClientThread(MCAST_GRP,MCAST_PORT) #Aqui la ip deberia ser 'servicio' y el puerto 5000
Datanode1.start()
#-----------------------------------------------------------------------

#-------------------------Manejo cliente--------------------------------
ser_cli = socket.socket()   
ser_cli.bind(('headnode', 5004)) 
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
