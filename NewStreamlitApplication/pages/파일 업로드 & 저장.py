import streamlit as st
import sqlite3
import os
import pandas as pd
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

제목_작성_도구("오잉")

t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    p = 파일_업로더_도구("파일 업로드")
    p.데이터프레임_생성()
    p.데이터베이스_저장()

    QUERY = f"""
    SELECT a.DATE, a.Round, a.Team, a.Opponent, a.Result, b.Player, b.Pos
    FROM matches a
    LEFT JOIN second.{uploaded_file} b ON a.Team = b.Team;
    """
    dataset = t.SELECT(QUERY)
    # 👉 DataFrame 생성
    df = pd.DataFrame(dataset, columns=['Date', 'Round', 'Team', 'Opponent', 'Result', 'Player', 'Pos'])

    # 👉 데이터 표시
    DF_표기_도구(df, "fix?", True)

else:
    st.error("CSV 파일만 업로드해주세요.")



