import streamlit as st
import pandas as pd
import numpy as np
from tools.sqlite_tool import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()

# 👉 SQL 쿼리에 LIMIT 반영
QUERY = f"""
SELECT full_name, age
FROM players;
"""

# 👉 SQLite에서 데이터 가져오기
dataset = t.EXECUTE(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset, columns=['full_name', 'age'])


# 👉 데이터 표시
if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
