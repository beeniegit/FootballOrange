import streamlit as st
import sqlite3
import random
import time
from 도구.SQLITE_클래스 import SQLITE_도구
from 도구.STREAMLIT_도구 import *

# 페이지 제목
st.write("채팅 기능")

# 주석
st.caption("데모임 꼬우면 나가")

# 로그인
if "username" not in st.session_state:
    st.session_state.username = st.text_input("Enter your name to join the chat:")
    st.stop()  # 입력 전까지 실행 중단

# 도구 인스턴스 생성
t = SQLITE_도구("/root/git/project/FootballOrange/NewStreamlitApplication/도구/chat.db")

# 데이터베이스 연결 및 db에 채팅 저장
conn = t.연결()
cursor = conn.cursor()
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS messages (
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    username TEXT,
    message TEXT
)
""")
conn.commit()

# 채팅 시작 및 기본 메세지 출력
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# 저장된 채팅 기록 불러오기
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 채팅 입력
if prompt := st.chat_input("Write message..."):

    # # 자동 새로고침(안돼 ㅠㅠ)
    # streamlit_autorefresh.streamlit_autorefresh(interval= 3000, key= "refresh")

    # 입력된 데이터 저장
    cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)",
                   (st.session_state.username, prompt))
    conn.commit()
    st.session_state.messages.append({"role": "user", "content": f"{st.session_state.username} : {prompt}"})

    # 저장된 채팅 기록 불러오기
    # cursor.execute("SELECT timestamp, username, message FROM messages ORDER BY timestamp DESC LIMIT 50")
    # messages = cursor.fetchall()
    # for ts, user, msg in reversed(messages):
    #     with st.chat_message("user" if user == st.session_state.username else "assistant"):
    #         st.markdown(f"**{user}**: {msg}")





