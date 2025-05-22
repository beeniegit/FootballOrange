import streamlit as st
import pandas as pd
import numpy as np
import datetime
from 도구.SQLITE_도구  import SQLITE_도구
from 도구.STREAMLIT_도구 import *

제목_작성_도구("아잉")

t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches;
"""

슬라 = 슬라이더_도구("MatchWeek", 1, 38, 1)

QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches
WHERE Round = '{f'Matchweek {슬라}'}'
ORDER BY Date ASC;
"""
dataset = t.SELECT(QUERY)
# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Round', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
DF_표기_도구(df, "데이터:", False)
