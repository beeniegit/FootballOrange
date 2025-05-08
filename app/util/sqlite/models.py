from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    이름 = Column(String, index=True)
    팀 = Column(String, index=True)
    포지션 = Column(String)
    나이 = Column(Integer)
    골 = Column(Integer)
