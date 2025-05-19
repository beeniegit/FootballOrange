import sqlite3

# 일반적인 Database :: Server Application
# SQLite Database :: File

class SqliteTool:

    # 생성자(인스턴스 생성)
    # 변수 정의
    def __init__(self):
        # DB 연결 객체
        self.connection = None
        # DB 연결 상태를 Boolean 으로 저장
        self.is_connected = False

    # 데이터베이스에 연결
    def connect(self):
        # 이미 연결이 되어 있으면 Pass
        if self.is_connected:
            return

        # 연결 시도
        self.connection = sqlite3.connect('/root/git/project/FootballOrange/NewStreamlitApplication/tools/matches.db')
        self.is_connected = True

    # QUERY 로 데이터 조회
    def EXECUTE(self, QUERY:str):
        if not self.is_connected:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute(QUERY)
        rows = cursor.fetchall()
        return rows

    # QUERY 로 데이터 패치
    def COMMIT(self, QUERY:str):
        if not self.is_connected:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute(QUERY)
        self.connection.commit()

    def attach_db(self, db_path: str, alias: str):
        if not self.is_connected:
            self.connect()
        cursor = self.connection.cursor()
        cursor.execute(f"ATTACH DATABASE '{db_path}' AS {alias}")
