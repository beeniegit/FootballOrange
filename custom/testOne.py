import streamlit as st
import pandas as pd
import numpy as np
from sqliteSample import SqliteTool

st.write("테스트용 메세지")

t = SqliteTool()
QUERY = f"""
SELECT Player, Team, Age, Pos, MP, Starts, Gls, Ast, CrdY, CrdR
FROM players;
"""
result = t.EXECUTE(QUERY)
size = len(result)

# 👉 슬라이더로 행 수 선택
num_rows = st.slider("Number of rows", 1, size, size//2)

# 👉 SQL 쿼리에 LIMIT 반영
QUERY = f"""
SELECT Player, Team, Age, Pos, MP, Starts, Gls, Ast, CrdY, CrdR
FROM players
ORDER BY Team DESC
LIMIT {num_rows};
"""

# 👉 SQLite에서 데이터 가져오기
dataset2 = t.EXECUTE(QUERY)

# 👉 DataFrame 생성
df = pd.DataFrame(dataset2, columns=['Player', 'Team', 'Age', 'Pos', 'MP', 'Starts', 'Gls', 'Ast', 'CrdY', 'CrdR'])

# 👉 나이 컬럼에 대한 설정
config = {
    "Age": st.column_config.ProgressColumn(),
}

# 👉 데이터 표시
if st.toggle("Enable editing"):
    edited_data = st.data_editor(df, column_config=config, use_container_width=True)
else:
    st.dataframe(df, column_config=config, use_container_width=True)
