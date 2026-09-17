from socket import * #Imports all socket functions and constants 

#CREATING SOCKET 

serverName = 'localhost' #set the server's hostname to the local computer
serverPort = 12000 #Port num used by the server

clientSocket = socket(AF_INET, SOCK_STREAM) #Create a IPv4 TCP Socket
clientSocket.connect((serverName, serverPort)) #Connect client to server

#USER MSG LOGIC

sentence = input('Enter lowercase sentence:') #Ask the user for a msg
clientSocket.send(sentence.encode())
sentenceModified = clientSocket.recv(1024).decode() #Recieve and decode the server

print('From Server:', sentenceModified) #Display the server's reponse

clientSocket.close()