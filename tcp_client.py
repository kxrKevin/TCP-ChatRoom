import sys
import socket
import argparse
import select
import threading
# Assignment: TCP Simple Chat Room - TCP Client Code Implementation

# **Libraries and Imports**: 
#    - Import the required libraries and modules. 
#    You may need sys, socket, argparse, select, threading (or _thread) libraries for the client implementation.
#    Feel free to use any libraries as well.

# **Global Variables**:
#    - IF NEEDED, Define any global variables that will be used throughout the code.

# **Function Definitions**:
#    - In this section, you will implement the functions you will use in the client side.
#    - Feel free to add more other functions, and more variables.
#    - Make sure that names of functions and variables are meaningful.
#    - Take into consideration error handling, interrupts,and client shutdown.

def text():
    while True:

        prompt = input("")

        if(prompt == '/exit'):
            client_socket.close()
            break

        message = client_name + ": " + prompt + "\n"
        client_socket.send(message.encode('ascii'))

def run(clientSocket, clientname):

    while True:
        try:
            message = clientSocket.recv(1024).decode('ascii')
            if message == 'username request':
                clientSocket.send(clientname.encode('ascii'))
                pass
            else:
                print(message)
        except:
            print("Disconnected From Server")
            clientSocket.close()
            break
    pass

# **Main Code**:  
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Argument Parser')
    parser.add_argument('name')  # to use: python tcp_client.py username
    args = parser.parse_args()
    client_name = args.name
    server_addr = '127.0.0.1'
    server_port = 9301

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    client_socket.connect((server_addr, server_port))

    receiveThread = threading.Thread(target=run, args=(client_socket, client_name))
    receiveThread.start()

    writeThread = threading.Thread(target=text)
    writeThread.start()
 