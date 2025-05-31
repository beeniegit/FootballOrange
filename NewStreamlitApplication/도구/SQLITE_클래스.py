import sqlite3
import pandas as pd
from 도구.DATABASE_인터페이스 import DATABASE_인터페이스


# 일반적인 Database :: Server Application
# SQLite Database :: File

class SQLITE_도구(DATABASE_인터페이스):

    # 생성자(인스턴스 생성)
    # 변수 정의
    def __init__(self, 경로:str):
        # DB 연결 객체
        self.연결_객체 = None
        # DB 연결 상태를 Boolean 으로 저장
        self.연결_여부 = False
        self.경로 = 경로

    # 데이터베이스에 연결
    def 연결(self):
        # 이미 연결이 되어 있으면 Pass
        if self.연결_여부:
            return

        # 연결 시도
        self.연결_객체 = sqlite3.connect(self.경로)
        self.연결_여부 = True
        return self.연결_객체

    # QUERY 로 데이터 조회
    def SELECT(self, QUERY:str):
        if not self.연결_여부:
            self.연결()

        cursor = self.연결_객체.cursor()
        cursor.execute(QUERY)
        rows = cursor.fetchall()
        return rows

    # QUERY 로 데이터 패치
    def RUN(self, QUERY:str):
        if not self.연결_여부:
            self.연결()

        cursor = self.연결_객체.cursor()
        cursor.execute(QUERY)
        self.연결_객체.commit()

    # csv 파일을 읽고 테이블 생성
    def DF_TABLE_생성(self, 데이터프레임:pd.DataFrame, 테이블명:str):
        if not self.연결_여부:
            self.연결()

        데이터프레임.to_sql(테이블명, self.연결_객체, if_exists='replace', index=False)
