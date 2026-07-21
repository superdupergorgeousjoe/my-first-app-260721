import os
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import font_manager as fm

st.set_page_config(page_title="데이터 시각화", page_icon="📊", layout="wide")

# 한글 폰트 설정 (fonts 폴더에 자동 다운로드하여 사용)
FONT_DIR = os.path.join(os.path.dirname(__file__), "..", "fonts")
FONT_PATH = os.path.join(FONT_DIR, "NotoSansKR.ttf")
FONT_URL = "https://github.com/google/fonts/raw/main/ofl/notosanskr/NotoSansKR%5Bwght%5D.ttf"
os.makedirs(FONT_DIR, exist_ok=True)
if not os.path.exists(FONT_PATH):
  urllib.request.urlretrieve(FONT_URL, FONT_PATH)
fm.fontManager.addfont(FONT_PATH)
font_prop = fm.FontProperties(fname=FONT_PATH)
plt.rcParams["font.family"] = font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

st.title("📊 데이터 시각화 예시")
st.markdown("이 페이지에서는 다양한 차트를 보여주고, 데이터를 직접 조작해 볼 수 있습니다.")

# 샘플 데이터
months = ["1월", "2월", "3월", "4월", "5월", "6월"]
rng = np.random.default_rng(42)
sales = rng.integers(50, 150, size=6)
df = pd.DataFrame({"월": months, "매출": sales})

st.subheader("월별 매출 그래프 (matplotlib)")
fig, ax = plt.subplots()
ax.plot(df["월"], df["매출"], marker="o")
ax.set_title("2026년 상반기 매출")
ax.set_xlabel("월")
ax.set_ylabel("매출 (단위: 만원)")
ax.grid(True)
st.pyplot(fig)

st.subheader("Streamlit 기본 차트")
col1, col2 = st.columns(2)
with col1:
  st.caption("막대 그래프")
  st.bar_chart(df.set_index("월"))
with col2:
  st.caption("영역 그래프")
  st.area_chart(df.set_index("월"))
st.divider()

st.header("✏️ 직접 데이터를 입력해 보세요")
st.write("아래 표의 값을 더블클릭해서 수정하면 차트가 바로 바뀝니다!")
edited_df = st.data_editor(df, use_container_width=True, num_rows="dynamic")

chart_type = st.radio("차트 종류 선택:", ["선 그래프", "막대 그래프"], horizontal=True)
plot_df = edited_df.dropna().set_index("월")
if chart_type == "선 그래프":
  st.line_chart(plot_df)
if chart_type == "막대 그래프":
  st.bar_chart(plot_df)
