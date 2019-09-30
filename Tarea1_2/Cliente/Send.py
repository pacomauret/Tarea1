import socket

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#command = "bridge test!"
#adress= ('recieve', 5000)
#sock.connect(('server', 5000))
#sock.sendall(command.encode())
#sock.close() 
  
s = socket.socket()   
s.connect(('server', 5000))  
  
while True:  
      mensaje = "quit"
      s.sendall(mensaje.encode()) 
      if mensaje == "quit":  
         break  
  
print("adios")  
  
s.close() 
