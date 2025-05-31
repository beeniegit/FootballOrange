from abc import ABC, abstractmethod
from sqlalchemy import create_engine
import pandas as pd


class DATABASE_인터페이스(ABC):


    # 데이터베이스에 연결
    @abstractmethod
    def 연결(self, *args, **kwargs):
        pass


    # QUERY 로 데이터 조회
    @abstractmethod
    def SELECT(self, QUERY: str):
        pass


    # QUERY 로 데이터 패치
    @abstractmethod
    def RUN(self, QUERY: str):
        pass


    # csv 파일을 읽고 테이블 생성
    @abstractmethod
    def DF_TABLE_생성(self, 데이터프레임: pd.DataFrame, 테이블명: str):
            pass

