import socket #UDP Client
if __name__ == '__main__':
    serverName = 'localhost' #IP 주소
    serverPort = 18000 #Port 주소
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    while True:
        print('Client >> ', end='')
        send_data = bytes(input().encode()) #사용자 입력
        clientSocket.sendto(send_data, (serverName, serverPort)) 
        recv_data, addr = clientSocket.recvfrom(2048)
        print('Server >> ' + str(recv_data.decode()))
        
        
        
import socket #UDP Server
if __name__ == '__main__':
    serverName = '' #IP 주소
    serverPort = 18000 #Port 주소
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverName, serverPort))

    while True:
        data, addr = serverSocket.recvfrom(2048) 
        print('Client >> ' + str(data))
        serverSocket.sendto(data.lower(), (addr)) 
