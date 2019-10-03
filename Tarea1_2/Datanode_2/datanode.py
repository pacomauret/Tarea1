from threading import Thread 
from socketserver import ThreadingMixIn 
import socket
import time
import struct
import sys
from datetime import datetime


class ClientThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 

    def run(self):

        multicast_group = '224.3.29.71'
        server_address = ('', 5000)
        IS_ALL_GROUPS = False

                # Create the socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind to the server address
        if IS_ALL_GROUPS:
          # on this port, receives ALL multicast groups
          sock.bind(server_address)
        else:
          # on this port, listen ONLY to MCAST_GRP
          sock.bind((multicast_group, 5000))

        # Tell the operating system to add the socket to
        # the multicast group on all interfaces.

        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        # Receive/respond loop
        while True:
            data, address = sock.recvfrom(1024)
            mensaje = 'Datanode2'
            sock.sendto(mensaje.encode(), address)
            

#----------------------Multicast Thread---------------------------------
MCAST_GRP = '224.3.29.71'
MCAST_PORT = 5001
#Thread multicast se inicia en un principio para comenzar a pingear a los datanodes
Datanode1 = ClientThread(MCAST_GRP,MCAST_PORT) #Aqui la ip deberia ser 'servicio' y el puerto 5000
Datanode1.start()
#-----------------------------------------------------------------------


s = socket.socket()   
s.connect(('headnode', 5002))
  
while True:
  #mensaje = input("Enter Employee Name")
  #s.sendall(mensaje.encode())

  recibido = bytes.decode(s.recv(1024))
  print ("recibido =",recibido)
  if (recibido!="" and recibido !="quit"):
    hora = datetime.now()
    horita = hora.strftime("%d/%m/%Y %H:%M:%S")
    file = open("data.txt","a")
    file.write("[" + horita + "] Se recibio el mensaje: " + recibido + ", desde el servidor\n")
    file.close()
  ok='guardado!'
  s.sendall(ok.encode())
  if (recibido=='quit'):
  	
  	break
  #if recibido == "saliendo": 
  #  break  
  
print("Cerrando Datanode")  
  
s.close()

Datanode1.join()