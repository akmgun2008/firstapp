import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 로드
df = pd.read_csv("vgsales.csv")

# 데이터 전처리
# 퍼블리셔별 글로벌 판매량 합산 후 상위 5개
top_publishers = (
    df.groupby("Publisher")["Global_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

# Streamlit UI
st.title("Top 5 Game Publishers by Global Sales")
st.write("데이터: vgsales.csv")

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
