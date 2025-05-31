from pymongo import MongoClient
import pandas as pd

from NewStreamlitApplication.도구.DATABASE_인터페이스 import DATABASE_인터페이스


class MONGO_DB_클래스(DATABASE_인터페이스):

    # 생성자(인스턴스 생성)
    # 변수 정의
    def __init__(self, 연결_문자열: str, DB명: str, 컬렉션명: str):
        self.연결_문자열 = 연결_문자열
        self.DB명 = DB명
        self.컬렉션명 = 컬렉션명
        self.client = None
        self.db = None
        self.collection = None
        self.연결_여부 = False

    def 연결(self):
        if self.연결_여부:
            return
        self.client = MongoClient(self.연결_문자열)
        self.db = self.client[self.DB명]
        self.collection = self.db[self.컬렉션명]
        self.연결_여부 = True

    def SELECT(self, 조건: dict):
        if not self.연결_여부:
            self.연결()
        return list(self.collection.find(조건))

    def INSERT(self, 데이터: dict):
        if not self.연결_여부:
            self.연결()
        self.collection.insert_one(데이터)

    def DF_COLLECTION_생성(self, 데이터프레임: pd.DataFrame, 컬렉션명: str):
        raise Exception("에러")
