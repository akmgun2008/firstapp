import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.title("🔋 Global EV Sales Dashboard")
st.write("데이터 출처: IEA - EV Sales Historical Cars")

# CSV 로드
df = pd.read_csv("IEA-EV-dataEV salesHistoricalCars - IEA-EV-dataEV salesHistoricalCars.csv")

# EV sales 데이터만 필터링
df_sales = df[(df["parameter"] == "EV sales") & (df["unit"] == "Vehicles")]

# 연도별 글로벌 총합
global_sales = df_sales.groupby("year")["value"].sum().reset_index()

# 지역 선택
regions = df_sales["region"].unique()
selected_regions = st.multiselect(
    "지역을 선택하세요 (비어있으면 전체):",
    options=regions,
    default=[],
)

# 선택한 지역 필터
if selected_regions:
    filtered_df = df_sales[df_sales["region"].isin(selected_regions)]
    sales_by_year = filtered_df.groupby("year")["value"].sum().reset_index()
    title = f"선택한 지역: {', '.join(selected_regions)}"
else:
    sales_by_year = global_sales
    title = "Global EV Sales (All Regions)"

# Plotly 그래프
fig = px.line(
    sales_by_year,
    x="year",
    y="value",
    markers=True,
    title=title,
    labels={"year": "Year", "value": "EV Sales (Vehicles)"},
)

st.plotly_chart(fig, use_container_width=True)

# 원본 데이터 확인
with st.expander("🔍 원본 데이터 보기"):
    st.write(df.head())
