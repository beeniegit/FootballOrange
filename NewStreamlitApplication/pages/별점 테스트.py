import streamlit as st
import pandas as pd
import numpy as np
import datetime
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

st.write("테스트용 메세지")

t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches;
"""

팀 = 선택형_도구(
    "Select Team",
    ["Arsenal", "Aston Villa", "Bournemouth ", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton Town", "Manchester City", "Manchester United", "Newcastle Utd", "Nott'ham Forest", "Sheffield Utd", "Tottenham", "West Ham", "Wolves"]
)


평가용_도구("stars")

QUERY = f"""
SELECT Date, Venue, Team, Opponent, Result
FROM matches
WHERE Team = '{팀}'
ORDER BY Date ASC;
"""
dataset = t.SELECT(QUERY)
# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
DF_표기_도구(df, "편집 ㄱㄱ", True)
