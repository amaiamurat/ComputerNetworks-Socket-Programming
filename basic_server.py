from socket import *

#CREATE AND BIND SOCKET 

serverPort = 12000 #Set the server port num
serverSocket = socket(AF_INET, SOCK_STREAM) #Create TCP Socket using IPv4 
serverSocket.bind(('', serverPort)) #Bind the server socket to port num

#LISTENING 
serverSocket.listen(1) #Listen for client connections
print('The server is ready to recieve') #Confirm the server is running

while True:

    connectionSocket, addr = serverSocket.accept() #Accept connection from the client
    sentence = connectionSocket.recv(1024).decode() #Recieve and decode the client msg

    #FORMATTING

    sentenceCapitalized = sentence.upper()
    connectionSocket.send(sentenceCapitalized.encode())
