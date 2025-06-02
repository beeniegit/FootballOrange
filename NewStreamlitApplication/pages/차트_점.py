import streamlit as st
import pandas as pd
from 도구.STREAMLIT_도구 import *

t = 파일_업로더_도구("파일 업로드")

df = t.데이터프레임_생성()

df_request = df[['goals_overall', 'assists_overall']]

st.scatter_chart(df_request)






