import streamlit as st
import plotly.express as px

# 제목
st.title("포켓몬 인기도 TOP 5")

# 데이터 예시 (원하는 데이터로 바꿔주세요)
pokemon = ["피카츄", "리자몽", "이브이", "뮤", "뮤츠"]
popularity = [95, 90, 85, 80, 75]

# Plotly Bar Chart
fig = px.bar(
    x=pokemon,
    y=popularity,
    labels={'x': '포켓몬', 'y': '인기도'},
    title="포켓몬 인기도 순위"
)

# 그래프 출력
st.plotly_chart(fig)
