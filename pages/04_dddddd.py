import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🔋 Electric Vehicle Sales Dashboard")
st.write("데이터: IEA EV Sales Historical Cars")

# CSV 파일 로드
df = pd.read_csv("IEA-EV-dataEV salesHistoricalCars.csv")

# 데이터 구조 확인
st.write("## Raw Data")
st.write(df.head())

# 연도별 판매량 합계 계산 (예: Column 이름에 따라 조정)
# 예: 'Year' 컬럼과 'Value' 컬럼이 있다고 가정
if 'Year' in df.columns and 'Value' in df.columns:
    sales_by_year = df.groupby("Year")["Value"].sum().reset_index()

    fig = px.line(
        sales_by_year,
        x="Year",
        y="Value",
        markers=True,
        title="📈 Global EV Sales Over Time",
        labels={"Value": "EV Sales (Units)"},
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("CSV 파일에 'Year' 또는 'Value' 컬럼이 없습니다.")
