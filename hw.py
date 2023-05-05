import os
import sys
from socket import *

PORT = int(sys.argv[1])
print("Student ID   :   20192806")
print("Name         :   Han Byeong Kyu")

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', PORT))
serverSocket.listen()


while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:    
        message = connectionSocket.recv(2048)
        print(f"message is : {message}")
        filename = message.split()[1]    
        f = open('.' + filename.decode(), 'rt', encoding='utf-8')
        outputdata = f.read()
        f.close()
        sendingData = 'HTTP/1.1 200 OK\n' + outputdata
        connectionSocket.send(sendingData.encode('utf-8'))
        print("OK!")
        connectionSocket.close()

    except IOError:
        # Send response message 'http status' for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found'.encode('utf-8'))
        #Close client socket 
        connectionSocket.close()
# close server socket 
serverSocket.close()