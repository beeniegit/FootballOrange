import streamlit as st

from 도구.STREAMLIT_도구 import 파일_업로더_도구
from 도구.SQLITE_도구 import SQLITE_도구

# SQLITE 객체 생성
SQLITE = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/matches.db")

# 파일 업로더 객체 생성
파일_업로더 = 파일_업로더_도구("파일을 업로드 해 주세요 :) CSV 파일을 읽고, 테이블을 생성합니다.")

# 업로드 된 파일이 있을 경우에만 실행
if 파일_업로더.파일:

    # 데이터프레임
    df = 파일_업로더.데이터프레임_생성()

    # 테이블 생성
    name = 파일_업로더.파일명
    SQLITE.DF_TABLE_생성(df, name)
    
    # 결과 안내
    st.success(f"테이블이 SQLite 데이터베이스에 저장되었습니다.")

else:

    # 오류 안내
    st.warning("CSV 파일을 업로드해주세요.")
