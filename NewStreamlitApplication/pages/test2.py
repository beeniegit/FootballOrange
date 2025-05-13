import streamlit as st
import pandas as pd
import numpy as np
import datetime
from tools.sqlite_tool import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()

d = st.date_input("Select Date", value=None)

if d:
    d_str = d.strftime('%Y-%m-%d')
    QUERY = f"""
    SELECT Date, Venue, Team, Opponent, Result
    FROM matches
    WHERE Date = '{d_str}'
    ORDER BY Date ASC;
    """
    st.write("Date:", d_str)
else:
    QUERY = f"""
    SELECT Date, Venue, Team, Opponent, Result
    FROM matches;
    """
    st.warning("Select Date")

# 👉 SQLite에서 데이터 가져오기
print(QUERY)
dataset = t.EXECUTE(QUERY)
print(len(dataset))

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['Date', 'Venue', 'Team', 'Opponent', 'Result'])


# 👉 데이터 표시
if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
