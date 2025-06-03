import streamlit as st
import pandas as pd
from 도구.STREAMLIT_도구 import *

# 파일 업로드, 인스턴스 생성
t = 파일_업로더_도구("파일 업로드")

# 데이터프레임 생성
df = t.데이터프레임_생성()

# 조건부 데이터 추출
df_request = df[['goals_overall', 'assists_overall']]

# 데이터 시각화
st.line_chart(df_request)






