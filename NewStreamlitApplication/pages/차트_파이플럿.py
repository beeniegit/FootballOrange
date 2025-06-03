import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from 도구.STREAMLIT_도구 import *

# 파일 업로드, 인스턴스 생성
t = 파일_업로더_도구("파일 업로드")

# 데이터프레임 생성
df = t.데이터프레임_생성()

# 데이터 가져오기
df_request = df["full_name"].head(5)
y = df["goals_overall"].head(5)
fig, ax = plt.subplots()

# 데이터 원형 그래프로 만들기
ax.pie(y, labels=df_request, autopct='%1.1f%%')

# 찌그러짐 방지
ax.axis('equal')

# 데이터 시각화
st.pyplot(fig)






