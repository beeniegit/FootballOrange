import pandas as pd
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

# 제목 작성
제목_작성_도구("테스트 페이지입니다.")

# SQLITE 객체 생성
SQLITE = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# SELECT 쿼리 실행
QUERY = f"""
SELECT Date, Time
FROM matches;
"""
결과 = SQLITE.SELECT(QUERY)

# 결과의 크기 반환
크기 = len(결과)

# 슬라이더 :: 개수 반환
개수 = 슬라이더_도구("Number of rows", 1, 크기, 크기//2)

# SELECT 쿼리 실행
QUERY = f"""
SELECT Date, Venue, Team, Opponent, Result
FROM matches
ORDER BY Date DESC
LIMIT {개수};
"""
결과 = SQLITE.SELECT(QUERY)

# 데이터프레임 생성
df = pd.DataFrame(결과, columns=['Date', 'Venue', 'Team', 'Opponent', 'Result'])

# DF 표기
DF_표기_도구(df, "내용을 편집할 수 있습니다 :)", True)
