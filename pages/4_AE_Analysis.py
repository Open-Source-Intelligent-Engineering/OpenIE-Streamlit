import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # 设置屏幕展开方式，宽屏模式布局更好

add_selectbox = st.sidebar.selectbox(
    'Which raw would you like to select? (Default raw is row1)',
    ('row1', 'row2', 'row3'))


st.markdown('## 机床主轴与台面噪声信号')
path = './data/mill.xlsx'

AE_spindle, AE_table = st.columns(2)
AE_spindle.markdown('#### 主轴噪声信号')
AE_spindle_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 6])
# print(AE_spindle_data)
c = alt.Chart(AE_spindle_data).mark_line().encode(x='index', y='AE_spindle')
AE_spindle.altair_chart(c, use_container_width=True)

AE_table.markdown('#### 台面噪声信号')
AE_table_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 5])
# print(AE_spindle_data)
c = alt.Chart(AE_table_data).mark_line().encode(x='index', y='AE_table')
AE_table.altair_chart(c, use_container_width=True)
