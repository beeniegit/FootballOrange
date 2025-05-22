import streamlit as st
import pandas as pd
import os

# 파일 업로더 도구
class 파일_업로더_도구:
    def __init__(self, 문구: str):
        # <속성> 파일
        self.파일 = st.file_uploader(문구, type=['csv'])

        # <속성> 파일명
        if self.파일:
            self.파일명 = os.path.splitext(self.파일.name)[0]
        else:
            self.파일명 = None

    # 데이터프레임 객체 생성 기능
    def 데이터프레임_생성(self):
        if self.파일:
            try:
                데이터프레임 = pd.read_csv(self.파일)
                return 데이터프레임
            except Exception as e:
                st.error(f"CSV 파일을 읽는 도중 오류가 발생했습니다: {e}")
                return None
        else:
            st.warning("파일이 업로드되지 않았습니다.")
            return None

# 제목 작성 도구
def 제목_작성_도구(문구:str):
    st.write(문구)

# 슬라이더 도구
def 슬라이더_도구(문구:str, 시작값:int, 끝값:int, 초기값:int):
    return st.slider(문구, 시작값, 끝값, 초기값)

# DF 표기 도구
def DF_표기_도구(데이터프레임:pd.DataFrame, 문구:str, 편집기능:bool):
    if 편집기능:
        if st.toggle(문구):
            st.data_editor(데이터프레임, use_container_width=True)
        else:
            st.dataframe(데이터프레임, use_container_width=True)
    else:
        st.dataframe(데이터프레임, use_container_width=True)

def 달력_도구(문구:str, 초기값:None):
    return st.date_input(문구, 초기값)

def 선택형_도구(문구:str, 선택박스:list):
    return st.radio(문구, 선택박스)

def 평가용_도구(방법:str):
    selected = st.feedback(방법)
    if selected == 0:
        st.markdown("???????")
    elif selected is None:
        st.markdown("Please give us a feedback.")
    else:
        st.markdown("Thank you for your feedback!")

