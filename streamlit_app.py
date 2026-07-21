import streamlit as st

# ===== 페이지 설정 =====
st.set_page_config(page_title="Streamlit 요소 예시", page_icon="🎨", layout="wide")

# ===== 사이드바 =====
st.sidebar.header("⚙️ 사이드바")
st.sidebar.write("이것은 사이드바입니다. 여기에 필터나 설정을 놓을 수 있습니다.")
sidebar_check = st.sidebar.checkbox("사이드바 체크박스")
sidebar_radio = st.sidebar.radio("사이드바 라디오:", ["옵션 1", "옵션 2"])
sidebar_slider = st.sidebar.slider("사이드바 슬라이더:", 0, 100, 50)

# ===== 제목 및 소개 =====
st.title("🎨 Streamlit 웹 애플리케이션 요소 전시")
st.markdown("""
이 페이지는 Streamlit에서 제공하는 주요 요소들을 보여주는 예시입니다.
왼쪽 사이드바에서 다른 페이지(자기소개, 데이터 시각화, 직접 해보기)로 이동할 수 있습니다.
""")

# ===== 텍스트 요소 =====
st.header("📄 텍스트 요소")

st.subheader("1. 제목과 마크다운")
st.markdown("**굵은 텍스트**, *이탤릭*, `코드`, [링크](https://streamlit.io)")
st.info("💡 정보 메시지")
st.success("✅ 성공 메시지")
st.warning("⚠️ 경고 메시지")
st.error("❌ 에러 메시지")

st.subheader("2. 코드 블록")
st.code("import streamlit as st\nst.write('Hello, Streamlit!')", language="python")

# ===== 입력 위젯 =====
st.header("🎛️ 입력 위젯")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("이름을 입력하세요")
    if name:
        st.write(f"안녕하세요, **{name}**님! 👋")

    number = st.number_input("숫자를 입력하세요", min_value=0, max_value=100, value=10)
    st.write(f"입력한 숫자의 제곱: {number ** 2}")

    if st.button("클릭해 보세요!"):
        st.balloons()
        st.write("🎈 풍선이 날아갑니다!")

with col2:
    color = st.selectbox("좋아하는 색을 골라 보세요", ["빨강", "주황", "노랑", "초록", "파랑"])
    st.write(f"선택한 색: {color}")

    level = st.slider("만족도를 선택하세요", 1, 5, 3)
    st.write("만족도:", "⭐" * level)

    agree = st.checkbox("체크박스에 동의합니다")
    if agree:
        st.write("동의해 주셔서 감사합니다! 😄")

# ===== 데이터 요소 =====
st.header("📊 데이터 요소")

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "과목": ["국어", "수학", "영어", "과학", "사회"],
    "점수": [85, 92, 78, 95, 88],
})

col3, col4 = st.columns(2)
with col3:
    st.subheader("표 (DataFrame)")
    st.dataframe(df, use_container_width=True)
with col4:
    st.subheader("차트 (Bar Chart)")
    st.bar_chart(df.set_index("과목"))

st.subheader("지표 (Metric)")
m1, m2, m3 = st.columns(3)
m1.metric("평균 점수", f"{df['점수'].mean():.1f}점", "+2.3")
m2.metric("최고 점수", f"{df['점수'].max()}점")
m3.metric("응시 과목", f"{len(df)}과목")

st.divider()
st.caption("마이크로디그리 융합교육을 위한 기초 프로그래밍 · 4일차 실습 · Streamlit 웹 애플리케이션 개발")
