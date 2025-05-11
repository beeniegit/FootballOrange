import streamlit as st
import pandas as pd
import numpy as np
from sqliteSample import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()

# 👉 SQL 쿼리에 LIMIT 반영
QUERY = f"""
SELECT Player
FROM players
ORDER BY Team DESC;
"""
result = t.EXECUTE(QUERY)
size = len(result)

# 👉 슬라이더로 행 수 선택
num_rows = st.slider("Number of rows", 1, size, size//2)

team = st.radio(
    "Select Nation",
    ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton Town", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur", "West Ham United", "Wolverhampton"],
    index=None,
)

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Player, Nation, Team
FROM players
WHERE Team = '{team}'
ORDER BY Player
LIMIT {num_rows};
"""
dataset = t.EXECUTE(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Player','Nation', 'Team'])

# 👉 데이터 표시
st.bar_chart(df, x='Player', y='Nation', horizontal=True)
