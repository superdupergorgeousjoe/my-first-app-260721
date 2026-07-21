import streamlit as st

# ===== 실습 과제 1: 자기소개 페이지 =====
st.set_page_config(page_title="자기소개", page_icon="🙋", layout="centered")

st.title("🙋 자기소개")

col1, col2 = st.columns([1, 2])

with col1:
  st.markdown(
    "<div style='font-size:110px; text-align:center;'>🧑‍💻</div>",
    unsafe_allow_html=True,
  )

with col2:
  st.subheader("심지효")
  st.write("안녕하세요! Streamlit으로 웹 애플리케이션을 만드는 것을 배우고 있습니다.")
  st.write("📧 이메일: changil.ms06@allip.kr")
  st.write("🏫 소속: [마이크로디그리] 융합교육을 위한 기초 프로그래밍")

st.divider()

st.header("💪 나의 관심사")
interests = {
  "프로그래밍": 60,
  "데이터 분석": 50,
  "웹 개발": 70,
  "인공지능 활용": 80,
}
for interest, value in interests.items():
  st.write(f"**{interest}**")
  st.progress(value)

st.divider()

st.header("📌 요즘 배우고 있는 것")
st.markdown("- Python 기초 프로그래밍\n- Streamlit 웹 애플리케이션 개발\n- GitHub로 코드 관리하기 (Commit & Push!)\n- 생성형 AI와 함께 코딩하기")

st.header("🎯 목표")
st.info("나만의 웹 애플리케이션을 만들어서 전 세계에 배포해 보기! 🌍")

st.divider()

st.header("💬 방명록")
message = st.text_input("저에게 하고 싶은 말을 남겨 주세요!")
if message:
  st.success(f"메시지 감사합니다! 😊 {message}")
