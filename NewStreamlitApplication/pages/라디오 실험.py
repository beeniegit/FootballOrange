import streamlit as st
import pandas as pd
import numpy as np
import datetime
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

# 제목 작성
제목_작성_도구("뿌잉")

# SQLITE 객체 생성
t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# SELECT 쿼리 실행
QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches;
"""

# 선택지 제공
팀 = 선택형_도구(
    "Select Team",
    ["Arsenal", "Aston Villa", "Bournemouth ", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton Town", "Manchester City", "Manchester United", "Newcastle Utd", "Nott'ham Forest", "Sheffield Utd", "Tottenham", "West Ham", "Wolves"]
)

# 쿼리 실행
QUERY = f"""
SELECT Date, Venue, Team, Opponent, Result
FROM matches
WHERE Team = '{팀}'
ORDER BY Date ASC;
"""
# 반환
dataset = t.SELECT(QUERY)
# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
DF_표기_도구(df, "편집 ㄱ?", True)
