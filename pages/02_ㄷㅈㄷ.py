import streamlit as st
import plotly.express as px

# 제목
st.title("2-7 능력치 순위")

# 데이터
names = ["홍의찬", "이태완", "박희준", "신지용", "권예욱"]
# GOAT 순위는 보통 높은 순위가 더 높다고 가정, 점수로 표현
scores = [5, 4, 3, 2, 1]

# Plotly Bar Chart
fig = px.bar(
    x=names,
    y=scores,
    labels={'x': '이름', 'y': 'GOAT 순위 점수'},
    title="2-7 GOAT TOP 5"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
