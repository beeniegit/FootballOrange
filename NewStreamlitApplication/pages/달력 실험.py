import streamlit as st
import pandas as pd
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

제목_작성_도구("시발더워")

# SQLITE 객체 생성
t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 달력 도구
d = 달력_도구("날짜 골라", None)

# 날짜 고른거에 따라 쿼리 실행
if d:
    d_str = d.strftime('%Y-%m-%d')
    QUERY = f"""
    SELECT Date, Venue, Team, Opponent, Result
    FROM matches
    WHERE Date = '{d_str}'
    ORDER BY Date ASC;
    """
    st.write("Date:", d_str)
else:
    QUERY = f"""
    SELECT Date, Venue, Team, Opponent, Result
    FROM matches;
    """
    st.warning("Select Date")

# 👉 SQLite에서 데이터 가져오기
dataset = t.SELECT(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Venue', 'Team', 'Opponent', 'Result'])

# 데이터프레임 표기
DF_표기_도구(df, "편집하셈ㅋㅋ", True)