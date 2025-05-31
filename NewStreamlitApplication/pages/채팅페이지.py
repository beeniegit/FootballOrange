import streamlit as st
import sqlite3
import io
import random
from streamlit_autorefresh import st_autorefresh

def get_connection():
    conn = sqlite3.connect("chat.db", check_same_thread=False)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            username TEXT,
            message TEXT
        )
    """)
    return conn

conn = get_connection()
cursor = conn.cursor()

if "username" not in st.session_state:
    st.session_state.username = ""
if "profile_image_bytes" not in st.session_state:
    st.session_state.profile_image_bytes = None
if "default_icon" not in st.session_state:
    st.session_state.default_icon = random.choice(["👤", "🤖"])  # 기본 아이콘 랜덤 지정

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 실시간 채팅방")

if not st.session_state.username:
    st.subheader("👤 닉네임과 프로필 사진을 입력하세요")
    with st.form("login_form", clear_on_submit=False):
        nickname_input = st.text_input("닉네임")
        uploaded_image = st.file_uploader("프로필 사진 업로드", type=["jpg", "jpeg", "png"])
        submitted = st.form_submit_button("입장하기")

        if submitted and nickname_input.strip() != "":
            st.session_state.username = nickname_input.strip()
            if uploaded_image:
                st.session_state.profile_image_bytes = uploaded_image.read()
            else:
                st.session_state.profile_image_bytes = None
            # 기본 아이콘 새로 뽑기
            st.session_state.default_icon = random.choice(["👤", "🤖"])

if st.session_state.username:
    st.markdown(f"**{st.session_state.username}** 님, 환영합니다!")

    count = st_autorefresh(interval=3000, limit=None, key="chat_refresh")

    cursor.execute("SELECT timestamp, username, message FROM messages ORDER BY timestamp ASC")
    rows = cursor.fetchall()

    if len(rows) != len(st.session_state.messages):
        st.session_state.messages = rows

    st.subheader("📜 채팅 내역")

    for timestamp, user, message in st.session_state.messages:
        is_self = (user == st.session_state.username)
        cols = st.columns([1, 7])

        with cols[0]:
            if is_self:
                # 프로필 이미지 또는 기본 아이콘 출력
                if st.session_state.profile_image_bytes:
                    st.image(io.BytesIO(st.session_state.profile_image_bytes), width=40)
                else:
                    st.markdown(f"<div style='font-size:32px'>{st.session_state.default_icon}</div>", unsafe_allow_html=True)
            else:
                # 다른 사람은 기본 아이콘만 표시 (필요하면 DB에 프로필 사진 저장 구현 가능)
                st.markdown(f"<div style='font-size:32px'>👤</div>", unsafe_allow_html=True)

        with cols[1]:
            st.markdown(f"**{user}**: {message}")

    if prompt := st.chat_input("메시지를 입력하세요..."):
        st.session_state.messages.append((None, st.session_state.username, prompt))
        cursor.execute(
            "INSERT INTO messages (username, message) VALUES (?, ?)",
            (st.session_state.username, prompt)
        )
        conn.commit()
