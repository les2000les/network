import socket #TCP Client

if __name__ == '__main__':
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverName = 'localhost' #IP 주소
    serverPort = 22000 # Port 주소
    clientSocket.connect((serverName, serverPort)) 
    print('Connecting to ', serverName, serverPort)

    while True:
        print('Client >> ', end='')
        send_data = bytes(input().encode())
        clientSocket.send(send_data) 
        recv_data = clientSocket.recv(1024).decode()
        print('Server >> ' + str(recv_data))
       
     
    
import socket #TCP Server
if __name__ == '__main__':
    serverName = '' #IP
    serverPort = 22000 #Port
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    serverSocket.bind((serverName, serverPort)) 
    serverSocket.listen(1) 
    conn, addr = serverSocket.accept()
    print('Connected ' + str(addr))


    while True:
        data = conn.recv(1024) 
        print('Client >> ' + str(data))
        conn.sendall(data.upper())
