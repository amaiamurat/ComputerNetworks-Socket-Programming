from socket import *

#CREATE AND BIND SOCKET 

serverPort = 12000 #Set the server port num
serverSocket = socket(AF_INET, SOCK_STREAM) #Create TCP Socket using IPv4 
serverSocket.bind(('', serverPort)) #Bind the server socket to port num