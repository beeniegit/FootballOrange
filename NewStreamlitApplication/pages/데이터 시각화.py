import streamlit as st
import pandas as pd
import plost
from 도구.STREAMLIT_도구 import *

t = 파일_업로더_도구("파일 업로드 부탁")

df= t.데이터프레임_생성()

DF_표기_도구(df, "data", False)

df_name_age = df[['age', 'appearances_home', 'appearances_away']]

DF_표기_도구(df_name_age, "data", False)

st.area_chart(df_name_age)

st.bar_chart(df_name_age)

st.line_chart(df_name_age)

st.scatter_chart(df_name_age)

# st.pyplot(df_name_age)

# st.plotly_chart(df_name_age)

plost.line_chart(df_name_age, "age", ("appearances_home", "appearances_away"), pan_zoom='minimap')