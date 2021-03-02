# Import socket module  
import socket              
  
# Create a socket object  
s = socket.socket()          
  
# Define the port on which you want to connect  
port = 12345                
  
# connect to the server on local computer  
s.connect(('ec2-3-141-64-224.us-east-2.compute.amazonaws.com', port))  
  
# receive data from the server  
print (s.recv(1024).decode() ) 
# close the connection  
s.send(bytes('Thank you for connecting','utf-8'))
s.close()      
      