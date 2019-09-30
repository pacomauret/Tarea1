from threading import Thread 
from socketserver import ThreadingMixIn 
import socket
import time

class ClientThread(Thread): 

	def __init__(self,ip,port): 
		Thread.__init__(self) 
		self.ip = ip 
		self.port = port
		self.Datanodes = ["Datanode1","Datanode2","Datanode3"] 
		print("[+] New server socket thread started for " + ip + ":" + str(port)) 

	def run(self):
		if(self.ip == '224.1.1.1' ): #si esque es la thread para los pingeos constantes
			while True:
				for i in range(1,6):
					print(i)
					time.sleep(1)
				MULTICAST_TTL = 2
				mensaje = "holiwi"


				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
				
				sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

				sock.sendto(mensaje.encode(), (self.ip, self.port))
				try:
					print(bytes.decode(sock.recv(1024)))
				except sock.error:
					print("errorcetee")

				
				
				#sock.bind((self.ip, self.port))

				


    		

#----------------------Multicast Thread---------------------------------
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5001
#Thread multicast se inicia en un principio para comenzar a pingear a los datanodes
Datanode1 = ClientThread(MCAST_GRP,MCAST_PORT) #Aqui la ip deberia ser 'servicio' y el puerto 5000
Datanode1.start()
#-----------------------------------------------------------------------

#-------------------------Manejo cliente--------------------------------
"""TCP_IP = '' 
TCP_PORT = 5000 
BUFFER_SIZE = 1024  # Usually 1024, but we need quick response

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
Server.bind((TCP_IP, TCP_PORT)) 


#El servidor siempre debe estar escuchando en caso de una solicitud de un cliente
while True: 
    Server.listen(4) 
    print("Multithreaded Python server : Waiting for connections from clients...") 
    (conn, (ip,port)) = Server.accept() #coneccion de un cliente
    recibido = bytes.decode(Server.recv(1024))
    data = bytes.decode(conn.recv(2048)) 
    print("Server received data:" + data)
    MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
    conn.send(MESSAGE.encode())  # echo """

