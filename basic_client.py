from socket import * #Imports all socket functions and constants 

#CREATING SOCKET 

server_name = 'localhost' #set the server's hostname to the local computer
server_port = 46767 #Port num used by the server

client_socket = socket(AF_INET, SOCK_STREAM) #Create a IPv4 TCP Socket
client_socket.connect((server_name, server_port)) #Connect client to server

#USER MSG LOGIC

sentence = input('Enter lowercase sentence:') #Ask the user for a msg
client_socket.send(sentence.encode())
sentence_modified = client_socket.recv(1024).decode() #Recieve and decode the server

print('FROM SERVER:', sentence_modified) #Display the server's reponse

client_socket.close()

print("The client socket has closed.")