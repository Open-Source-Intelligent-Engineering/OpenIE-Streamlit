import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # 设置屏幕展开方式，宽屏模式布局更好

add_selectbox = st.sidebar.selectbox(
    'Which raw would you like to select? (Default raw is row1)',
    ('row1', 'row2', 'row3'))


st.markdown('## 刀具传感器电流信号')
path = './data/mill.xlsx'

# smcAC, smcDC = st.columns(2)
# smcAC.markdown('#### 主轴交流电信号')
# smcAC_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 1])
# # print(smcAC_data)
# c = alt.Chart(smcAC_data).mark_line().encode(x='index', y='smcAC')
# smcAC.altair_chart(c, use_container_width=True)

# smcDC.markdown('#### 主轴直流电信号')
# smcDC_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 2])
# # print(smcAC_data)
# c = alt.Chart(smcDC_data).mark_line().encode(x='index', y='smcDC')
# smcDC.altair_chart(c, use_container_width=True)
# smcAC, smcDC = st.columns(2)
st.markdown('#### 主轴交流电信号')
smcAC_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 1])
# print(smcAC_data)
c = alt.Chart(smcAC_data).mark_line().encode(x='index', y='smcAC',color=alt.value("#482ff7"))
st.altair_chart(c, use_container_width=True)

st.markdown('#### 主轴直流电信号')
smcDC_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 2])
# print(smcAC_data)
c = alt.Chart(smcDC_data).mark_line().encode(x='index', y='smcDC',color=alt.value("#2d6cdf"))
st.altair_chart(c, use_container_width=True)