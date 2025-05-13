import streamlit as st
import pandas as pd
import numpy as np
import datetime
from tools.sqlite_tool import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches;
"""

n = st.slider("Matchweek", 1, 38, 1)

QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches
WHERE Round = '{f'Matchweek {n}'}'
ORDER BY Date ASC;
"""
dataset = t.EXECUTE(QUERY)
# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Round', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
