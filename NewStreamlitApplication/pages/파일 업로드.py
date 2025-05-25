import streamlit as st
import sqlite3
import os
import pandas as pd
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

# 페이지 제목 작성
제목_작성_도구("끄악")

# 도구 인스턴스 생성
t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 파일 업로드
uploaded_file = st.file_uploader("Choose a file")

# 업로드 된 파일 읽고 데이터프레임으로
if uploaded_file is not None:
    p = 파일_업로더_도구("Upload File Please")
    p.데이터프레임_생성()

    # 쿼리 실행
    QUERY = f"""
    SELECT Date, Round, Venue, Team, Opponent, Result
    FROM matches;
    """
    # 데이터 추출
    dataset = t.SELECT(QUERY)
     # 👉 DataFrame 생성
    df = pd.DataFrame(dataset, columns=['Date', 'Round', 'Venue', 'Team', 'Opponent', 'Result'])

    # 👉 데이터 표시
    DF_표기_도구(df, "수정 가능?", True)

else:
    st.error("CSV 파일만 업로드해주세요.")



