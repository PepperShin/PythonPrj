from socket import *


host = "127.0.0.1" 
port = 12345 

client_socket = socket(AF_INET, SOCK_STREAM) # 소켓 생성
client_socket.connect((host, port)) # 서버 주소 정보 할당
    
print("연결확인 완료")

client_socket.send("안녕하세요. 저는 클라이언트입니다.".encode("utf-8")) # 서버에게 데이터 전송

data = client_socket.recv(1024) # 서버가 보낸 데이터 수신

print("받은 데이터 : " + data.decode("utf-8"))

client_socket.close() # 서버 소켓 닫기

