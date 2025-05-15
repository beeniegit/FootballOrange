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

venue = st.selectbox(
    "venue",
    ("Home", "Away"),
)

st.write("Selected: ", f'{venue}')

QUERY = f"""
SELECT Date,
       CAST(REPLACE(Round, 'Matchweek ', '') AS INTEGER) AS RoundNumber,
       Venue,
       Team,
       Opponent,
       Result
FROM matches
WHERE Venue = '{venue}'
ORDER BY RoundNumber ASC, Date ASC;

"""
dataset = t.EXECUTE(QUERY)
# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'RoundNumber', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)