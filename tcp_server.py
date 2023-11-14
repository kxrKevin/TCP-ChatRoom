import socket
import threading
import select
import time

# Assignment: TCP Simple Chat Room - TCP Server Code Implementation

# **Libraries and Imports**: 
#    - Import the required libraries and modules. 
#    You may need socket, threading, select, time libraries for the client.
#    Feel free to use any libraries as well.

# **Global Variables**:
#    - IF NEEDED, Define any global variables that will be used throughout the code.

# **Function Definitions**:
#    - In this section, you will implement the functions you will use in the server side.
#    - Feel free to add more other functions, and more variables.
#    - Make sure that names of functions and variables are meaningful.

def text(message):

    for client in clients:
        client.send(message.encode('ascii'))
        
def chat(client):
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            text(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            userName = userNames[index]
            text(userName + " has left the chat\n")
            print("User [" + userName + "] has disconnected")
            userNames.remove(userName)
            break

def run(serverSocket, serverPort):
    # The main server function.
    
    while True:

        clientSocket, addr = serverSocket.accept()
        clients.append(clientSocket)

        clientSocket.send('username request'.encode('ascii'))
        userName = clientSocket.recv(1024).decode('ascii')
        userNames.append(userName)

        print("Established Connection with " + userName + " from address: [" + str(addr) + "]")
        text("\n***" + userName + " joined the chat\n")

        thread = threading.Thread(target=chat, args=(clientSocket,))
        thread.start()

    pass

# **Main Code**:  
if __name__ == "__main__":
    server_port = 9301
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Creating a TCP socket.
    server_socket.bind(('127.0.0.1', server_port))
    server_socket.listen(3) # size of the waiting_queue that stores the incoming requests to connect.
    print("Server is listening.... ")

    clients = [] #list to add the connected client sockets , feel free to adjust it to other place
    userNames = []
    run(server_socket,server_port)# Calling the function to start the server.