import streamlit as st

# 사용자 설정
배너_링크 = "https://www.naver.co.kr/"
배너_배경 = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
배너_높이 = "200px"
배너_위치 = "center"  # 'left', 'center', 'right'
배너_글자 = "NAVER"
글자_색상 = "white"
글자_그림자 = "2px 2px 4px rgba(0,0,0,0.7)"  # 선택사항

# HTML 렌더링
st.markdown(
    f"""
    <div style="text-align: {배너_위치}; margin: 20px 0;">
        <a href="{배너_링크}" target="_blank" style="text-decoration: none;">
            <div style="
                background-image: url('{배너_배경}');
                background-size: cover;
                background-position: center;
                width: 100%;
                height: {배너_높이};
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                display: flex;
                align-items: center;
                justify-content: center;
                transition: transform 0.3s ease;
                cursor: pointer;
            " onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                <h2 style="
                    color: {글자_색상};
                    text-shadow: {글자_그림자};
                    font-size: 24px;
                    font-weight: bold;
                    margin: 0;
                ">
                    {배너_글자}
                </h2>
            </div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
