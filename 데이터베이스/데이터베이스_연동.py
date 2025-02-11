import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    host='localhost',
    user='scott',
    password='tiger',
    db='scott',
    charset='utf8'
)

# Connection 으로부터 Cursor 생성
# cursor 객체는 sql 문장을 실행하고 결과를 가져오는 역할
curs = conn.cursor()

# SQL문 실행
sql = "select * from emp"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall() # 튜플 형태로 리턴.
print(rows)     # 전체 row

for row in rows:
    print(row)

# 테이블 생성
# sql = 'CREATE TABLE users (id char(4), name char(15), email char(20))'
# curs.execute(sql)

# 데이터 입력
sql = "insert into users values ('1', '홍길동', 'hong@gmail.com')"
curs.execute(sql)

sql = "insert into users values ('2', '김길동', 'kim@gmail.com')"
curs.execute(sql)
conn.commit() # 커밋해야 한다.

conn.close()