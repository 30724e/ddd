
import pandas as pd

url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 로드
url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(url)

st.title("Plotly 시각화 예제")

st.write("데이터 미리보기")
st.dataframe(df.head())

# 컬럼 이름에 따라 적절히 변경하세요
x_column = st.selectbox("X축 선택", df.columns)
y_column = st.selectbox("Y축 선택", df.columns)

fig = px.line(df, x=x_column, y=y_column, title=f"{y_column} over {x_column}")
st.plotly_chart(fig)

