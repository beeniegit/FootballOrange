import streamlit as st
import sqlite3
import os
import pandas as pd
import numpy as np
from tools.sqlite_tool import SqliteTool
from io import StringIO

st.write("테스트용 메세지")

t = SqliteTool()

# 👉 SQLite에서 데이터 가져오기
QUERY = f"""
SELECT Date, Round, Venue, Team, Opponent, Result
FROM matches;
"""

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    if uploaded_file.name.lower().endswith('.csv'):
        st.success("CSV 파일이 업로드되었습니다.")

        # 👉 CSV 파일을 DataFrame으로 읽기
        dataframe = pd.read_csv(uploaded_file)
        st.dataframe(dataframe)

        # 👉 SQLite DB 연결 (파일로 저장)
        db_name = "uploaded_data.db"
        table_name = os.path.splitext(uploaded_file.name)[0]  # 파일 이름을 테이블 이름으로

        conn = sqlite3.connect(db_name)
        try:
            # 👉 DataFrame을 SQLite 테이블로 저장 (같은 이름이면 덮어씀)
            dataframe.to_sql(table_name, conn, if_exists='replace', index=False)
            st.success(f"'{table_name}' 테이블이 SQLite 데이터베이스에 저장되었습니다.")
        except Exception as e:
            st.error(f"데이터 저장 중 오류 발생: {e}")
        finally:
            conn.close()

        t.attach_db("uploaded_data.db", "second")

        QUERY = f"""
        SELECT DISTINCT a.Team, b.Player,a.PKatt, a.PK
        FROM matches a
        LEFT JOIN second.{table_name} b ON a.PKatt = b.PKatt AND a.PK = b.PK
        WHERE b.PK >= 1
        ORDER BY b.PK DESC;
        """
        dataset = t.EXECUTE(QUERY)
        # 👉 DataFrame 생성
        df = pd.DataFrame(dataset, columns=['Team','Player', 'PKatt', 'PK'])

        # 👉 데이터 표시
        if st.toggle("Enable editing"):
            edited_data = st.data_editor(df, use_container_width=True)
        else:
            st.dataframe(df, use_container_width=True)

    else:
        st.error("CSV 파일만 업로드해주세요.")



