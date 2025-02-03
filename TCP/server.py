from socket import *
#import socket

#서버 소켓 생성
host = "127.0.0.1" #자기 자신 로컬 아이피
port = 12345 # 포트 번호 = 프로그램 식별번호

server_socket = socket(AF_INET, SOCK_STREAM) # 소켓 생성
server_socket.bind((host, port)) # 소켓 주소 정보 할당
server_socket.listen() # 맵핑된 소켓을 연결 요청 대기 상태로 전환

print("서버 소켓 생성 및 바인딩 완료")

#클라이언트 접속 대기
client_socket, client_address = server_socket.accept() # 클라이언트 접속 대기 및 연결 수락

print(str(client_address) + " 클라이언트 접속 하였습니다")

data = client_socket.recv(1024) # 클라이언트가 보낸 데이터 수신
print("받은 데이터 : " + data.decode("utf-8"))

client_socket.sendall("안녕하세요. 저는 서버입니다.".encode("utf-8")) # 클라이언트에게 데이터 전송

server_socket.close() # 서버 소켓 닫기