import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🎮 Video Game Sales Dashboard")
st.write("데이터: vgsales - vgsales.csv")

# CSV 파일 로드
df = pd.read_csv("vgsales - vgsales.csv")

# 결측치 제거 (있다면)
df = df.dropna(subset=["Publisher", "Global_Sales"])

# 퍼블리셔별 글로벌 판매량 합산
top_publishers = (
    df.groupby("Publisher")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

# Plotly 그래프
fig = px.bar(
    top_publishers,
    x="Publisher",
    y="Global_Sales",
    color="Publisher",
    title="Top 5 Publishers by Global Sales",
    labels={"Global_Sales": "Global Sales (Million Units)"},
)

st.plotly_chart(fig, use_container_width=True)
