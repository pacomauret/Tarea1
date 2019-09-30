from threading import Thread 
from socketserver import ThreadingMixIn 
import socket
import time
import struct

class ClientThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print("[+] New server socket thread started for " + ip + ":" + str(port)) 

    def run(self):
        if(self.ip == '224.1.1.1' ): #si esque es la thread para los pingeos constantes
            while True:
                MULTICAST_TTL = 2
                mensaje = "holawa"

                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.bind((self.ip, self.port))

                mreq = struct.pack("4sl", socket.inet_aton(self.ip), socket.INADDR_ANY)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
                print(bytes.decode(sock.recv(1024)))

                mensaje = "Datanode3"
                sock.sendall(mensaje.encode())
            

#----------------------Multicast Thread---------------------------------
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5001
#Thread multicast se inicia en un principio para comenzar a pingear a los datanodes
Datanode1 = ClientThread(MCAST_GRP,MCAST_PORT) #Aqui la ip deberia ser 'servicio' y el puerto 5000
Datanode1.start()
#-----------------------------------------------------------------------

"""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# on this port, listen ONLY to MCAST_GRP
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
data = bytes.decode(sock.recv(2048)) 
print("Server received data:" + data)
MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
sock.send(MESSAGE.encode())  # echo """
