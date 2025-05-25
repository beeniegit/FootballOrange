import streamlit as st
import pandas as pd
import numpy as np
import datetime
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

# 페이지 제목 생성
제목_작성_도구("쩝쩝")

# 도구 인스턴스 생성
t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 선택지 생성
구장 = 골라봐_도구("venue", ("Home", "Away"))

# 선택된 정보 출력
제목_작성_도구("Selected: ", f'{구장}')

# 쿼리 작성
QUERY = f"""
SELECT Date,
       CAST(REPLACE(Round, 'Matchweek ', '') AS INTEGER) AS RoundNumber,
       Venue,
       Team,
       Opponent,
       Result
FROM matches
WHERE Venue = '{구장}'
ORDER BY RoundNumber ASC, Date ASC;

"""
dataset = t.SELECT(QUERY)
# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'RoundNumber', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
DF_표기_도구(df, "편집은 역시 프리미어 프로", True)