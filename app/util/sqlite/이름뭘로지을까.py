import sqlite3

# 일반적인 Database :: 서버를 통해 앱을 띄워서
# SQLite Database :: File

class SqliteTool:

    # init : 생성자 메서드
    # 변수 정의
    def __init__(self):
        # 데이터베이스를 연결 하는 객체
        self.connection = None
        # 데이터베이스 연결 상태를 Boolean(참, 거짓) 으로 저장
        self.is_connected = False

    # 데이터베이스에 연결
    def connect(self):
        # 이미 연결이 되어 있으면 Pass
        if self.is_connected:
            return

        # 연결 시도
        self.connection = sqlite3.connect('app/example.db')
        self.is_connected = True

    # SQL QUERY 를 통해 데이터 조회
    # 연결이 안되어 있으면 다시 연결 시도
    def EXECUTE(self, QUERY:str):
        if not self.is_connected:
            self.connect()

        # SQL QUERY 명령 전달 및 실행, 결과 반환
        cursor = self.connection.cursor()
        cursor.execute(QUERY)
        rows = cursor.fetchall()
        return rows

    # SQL QUERY 를 통해 데이터 패치
    def COMMIT(self, QUERY:str):
        # 연결이 안되어 있으면 다시 연결 시도
        if not self.is_connected:
            self.connect()
        # SQL QUERY 명령 전달 및 실행, 변경 사항 영구 저장
        cursor = self.connection.cursor()
        cursor.execute(QUERY)
        self.connection.commit()