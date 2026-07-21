import random

import streamlit as st

# ===== 실습 과제 2: 조작이 들어간 웹 애플리케이션 =====
st.set_page_config(page_title="직접 해보기", page_icon="🎮", layout="centered")

st.title("🎮 직접 해보기: 숫자 맞히기 게임")
st.write("컴퓨터가 1부터 100 사이의 숫자 하나를 생각했어요. 숫자를 입력하고 도전 버튼을 눌러 보세요!")

if "answer" not in st.session_state:
  st.session_state.answer = random.randint(1, 100)
  st.session_state.tries = 0
  st.session_state.hint = "첫 도전을 기다리고 있어요!"
guess = st.number_input("숫자를 입력하세요 (1~100)", min_value=1, max_value=100, value=50)
go = st.button("도전! 🚀", use_container_width=True, type="primary")

if go and guess < st.session_state.answer:
  st.session_state.tries += 1
  st.session_state.hint = "⬆️ 더 큰 숫자예요!"
if go and guess > st.session_state.answer:
  st.session_state.tries += 1
  st.session_state.hint = "⬇️ 더 작은 숫자예요!"
if go and guess == st.session_state.answer:
  st.session_state.tries += 1
  st.session_state.hint = f"🎉 정답! {st.session_state.tries}번 만에 맞혔어요! 새 게임이 시작됩니다."
  st.balloons()
  st.session_state.answer = random.randint(1, 100)
  st.session_state.tries = 0
st.info(st.session_state.hint)
st.caption(f"지금까지 시도: {st.session_state.tries}번")

st.divider()

st.header("➕ 보너스: BMI 계산기")
col1, col2 = st.columns(2)
with col1:
  height = st.number_input("키 (cm)", min_value=100.0, max_value=220.0, value=170.0, step=0.5)
with col2:
  weight = st.number_input("몸무게 (kg)", min_value=30.0, max_value=200.0, value=60.0, step=0.5)
bmi = weight / ((height / 100) ** 2)
st.metric("나의 BMI", f"{bmi:.1f}")
if bmi < 18.5:
  st.info("저체중 범위입니다.")
if 18.5 <= bmi < 23:
  st.success("정상 범위입니다! 👍")
if 23 <= bmi < 25:
  st.warning("과체중 범위입니다.")
if bmi >= 25:
  st.warning("비만 범위입니다. 건강 관리에 신경 써 보아요!")
st.caption("※ 참고용 수치입니다. (아시아-태평양 기준)")
