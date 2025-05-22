import streamlit as st
import pandas as pd
import sqlite3
import os
from tools.sqlite_tool import SqliteTool

t = SqliteTool()

uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # SQLite DB 연결
    db_name = "players.db"
    conn = sqlite3.connect(db_name)

    # 테이블 이름은 파일 이름에서 확장자 제거한 것
    table_name = os.path.splitext(uploaded_file.name)[0]

    # 저장
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

    st.success(f"'{table_name}' 테이블이 SQLite 데이터베이스에 저장되었습니다.")
else:
    st.warning("CSV 파일을 업로드해주세요.")

# if uploaded_file is not None:
#     # 첫 줄(헤더)만 리스트로 추출
#     header = next(csv.reader(io.StringIO(uploaded_file.getvalue().decode('utf-8'))))
#     st.write("Header (first line):", header)
#
#     # 전체 데이터프레임 읽기
#     df = pd.read_csv(uploaded_file)
#     st.dataframe(df)

QUERY = f"""
SELECT full_name, age
FROM players;
"""

dataset = t.EXECUTE(QUERY)

df = pd.DataFrame(dataset, columns=['full_name', 'age'])


