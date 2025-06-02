import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from 도구.STREAMLIT_도구 import *

t = 파일_업로더_도구("파일 업로드")

df = t.데이터프레임_생성()

df_request = df["full_name"].head(5)
y = df["goals_overall"].head(5)

fig, ax = plt.subplots()

ax.pie(y, labels=df_request, autopct='%1.1f%%')

ax.axis('equal')

st.pyplot(fig)






