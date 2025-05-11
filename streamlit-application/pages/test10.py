import streamlit as st
import pandas as pd
import numpy as np
from sqliteSample import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()

# 👉 SQL 쿼리에 LIMIT 반영
QUERY = f"""
SELECT Player, PKatt, PK
FROM players
WHERE PKatt > 0
ORDER BY Player;
"""
result = t.EXECUTE(QUERY)
size = len(result)

# 👉 슬라이더로 행 수 선택
num_rows = st.slider("Number of rows", 1, size, size//2)

select = st.radio(
    "Select What would you like to see",
    ["PK Try", "PK Success"],
    index=None,
)

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Player, PKatt, PK
FROM players
WHERE PKatt > 0
ORDER BY Player
LIMIT {num_rows};
"""
dataset = t.EXECUTE(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Player','PK Try','PK Success'])

# 👉 데이터 표시
if select == "PK Try":
    st.bar_chart(df, x='Player', y='PK Try', horizontal=True)
else:
    st.bar_chart(df, x='Player', y='PK Success', horizontal=True)
