from socket import *

#CREATE AND BIND SOCKET 

server_port = 46767 #Set the server port num
server_socket = socket(AF_INET, SOCK_STREAM) #Create TCP Socket using IPv4 

print('A server socket has been created.') #Denotes that the server socket has been created

server_socket.bind(('', server_port)) #Bind the server socket to port num

#LISTENING 

server_socket.listen(1) #Listen for client connections

print('The server is running and ready to receive.') #Confirm the server is running

while True:

    connection_socket, addr = server_socket.accept() #Accept connection from the client

    print("The server socket has connected to the client.") #Confirm client connection

    sentence = connection_socket.recv(1024).decode() #Recieve and decode the client msg

    print('FROM CLIENT:', sentence) #Display client msg
    #FORMATTING

    response = "Your message has been received, thank you!"

    #SEND RESPONSE MSG

    connection_socket.send(response.encode()) #Encode and send response to client

    connection_socket.close()

    print("The server socket has closed.")
