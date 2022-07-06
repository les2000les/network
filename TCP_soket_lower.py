import socket #TCP Client

if __name__ == '__main__':
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverName = 'localhost' #IP 주소
    serverPort = 20000 # Port 주소
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
    serverPort = 20000 #Port
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    serverSocket.bind((serverName, serverPort)) 
    serverSocket.listen(1) #소켓 연결, 여기서 파라미터는 접속수를 의미
    conn, addr = serverSocket.accept() #해당 소켓을 열고 대기
    print('Connected ' + str(addr))


    while True:
        data = conn.recv(1024) 
        print('Client >> ' + str(data))
        conn.sendall(data.lower()) 
