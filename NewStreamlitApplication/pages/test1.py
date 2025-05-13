import streamlit as st
import pandas as pd
import numpy as np
from tools.sqlite_tool import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()
QUERY = f"""
SELECT Date, Time
FROM matches;
"""
result = t.EXECUTE(QUERY)
size = len(result)

# 👉 슬라이더로 행 수 선택
num_rows = st.slider("Number of rows", 1, size, size//2)

# 👉 SQL 쿼리에 LIMIT 반영
QUERY = f"""
SELECT Date, Venue, Team, Opponent, Result
FROM matches
ORDER BY Date DESC
LIMIT {num_rows};
"""

# 👉 SQLite에서 데이터 가져오기
dataset = t.EXECUTE(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
