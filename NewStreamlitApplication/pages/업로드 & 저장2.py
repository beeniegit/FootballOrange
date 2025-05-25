import streamlit as st
import pandas as pd
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

제목_작성_도구("뜨악")

t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

uploaded_file = st.file_uploader("Choose a file")

# 파일 읽고
if uploaded_file is not None:
    p = 파일_업로더_도구("파일 업로드")
    p.데이터프레임_생성()
    p.데이터베이스_저장()

    # 쿼리 실행
    QUERY = f"""
    SELECT DISTINCT a.Team, b.Player,b.MP, b.Pos
    FROM matches a
    LEFT JOIN second.{uploaded_file} b ON a.Team = b.Team
    WHERE b.MP >= 10
    ORDER BY b.MP DESC;
    """
    dataset = t.SELECT(QUERY)
    # 👉 DataFrame 생성
    df = pd.DataFrame(dataset, columns=['Team','Player', 'MP', 'Pos'])

    # 👉 데이터 표시
    DF_표기_도구(df, "Fix You~",True)

else:
    st.error("CSV 파일만 업로드해주세요.")



