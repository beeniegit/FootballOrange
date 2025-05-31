import streamlit as st
import pandas as pd
import sqlite3
import os
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

t = SQLITE_도구()

uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file is not None:
    p = 파일_업로더_도구("파일 업로드")
    p.데이터프레임_생성()
    p.데이터베이스_저장()

else:
    st.warning("CSV 파일을 업로드해주세요.")

QUERY = f"""
SELECT full_name, age
FROM matches;
"""

dataset = t.SELECT(QUERY)

df = pd.DataFrame(dataset, columns=['full_name', 'age'])

DF_표기_도구(df, "ㅍㅈ", True)


