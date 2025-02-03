from socket import *


host = "localhost" #자기 자신 로컬 아이피
port = 55555 

server_socket = socket(AF_INET, SOCK_STREAM) # 소켓 생성
#socket.SO_REUSEADDR 옵션을 설정해주면 방금 사용하고 close한,
#port를 즉시 다시 사용
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_socket.bind((host, port)) # 소켓 주소 정보 할당
server_socket.listen(100) # 대기열을 100개로 맵핑된 소켓을 연결 요청 대기 상태로 전환

# 클라이언트 접속 대기
client_socket, client_address = server_socket.accept() # 클라이언트 접속 대기 및 연결 수락

print(str(client_address) + " 클라이언트 접속 하였습니다")

while True:
    data = client_socket.recv(1024) # 클라이언트가 보낸 데이터 수신
    print("받은 데이터 : " + data.decode("utf-8"))
    client_socket.sendall(data) # 클라이언트에게 데이터 전송