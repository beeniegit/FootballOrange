import streamlit as st
import pandas as pd
from 도구.SQLITE_도구 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

from NewStreamlitApplication.도구.STREAMLIT_도구 import DF_표기_도구

# 제목 작성
제목_작성_도구("뿌잉")

# 도구 인스턴스 생성
t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 파일 업로드
uploaded_file = st.file_uploader("Choose a file")

# 파일 저장 및 데이터프레임 화
if uploaded_file is not None:
    p = 파일_업로더_도구("파일 업로드")
    p.데이터프레임_생성()
    p.데이터베이스_저장()

    # 쿼리 실행
    QUERY = f"""
    SELECT DISTINCT a.Team, b.Player,a.PKatt, a.PK
    FROM matches a
    LEFT JOIN second.{uploaded_file} b ON a.PKatt = b.PKatt AND a.PK = b.PK
    WHERE b.PK >= 1
    ORDER BY b.PK DESC;
    """
    dataset = t.SELECT(QUERY)
    # 👉 DataFrame 생성
    df = pd.DataFrame(dataset, columns=['Team','Player', 'PKatt', 'PK'])

    # 👉 데이터 표시
    DF_표기_도구(df, "유수정", True)

else:
    st.error("CSV 파일만 업로드해주세요.")



