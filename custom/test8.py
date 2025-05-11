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

select = st.radio(
    "Select What would you like to see",
    ["Match Point", "Starting"],
    index=None,
)

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Player, MP, Starts
FROM players
ORDER BY Player
LIMIT {num_rows};
"""
dataset = t.EXECUTE(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Player','MP','Starts'])

# 👉 데이터 표시
if select == "Match Point":
    st.bar_chart(df, x='Player', y='MP', horizontal=True)
else:
    st.bar_chart(df, x='Player', y='Starts', horizontal=True)
