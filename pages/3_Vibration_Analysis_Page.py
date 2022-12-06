import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # 设置屏幕展开方式，宽屏模式布局更好

add_selectbox = st.sidebar.selectbox(
    'Which raw would you like to select? (Default raw is row1)',
    ('row1', 'row2', 'row3'))


st.markdown('## 机床主轴与台面振动信号')
path = './data/mill.xlsx'

# vib_spindle, vib_table = st.columns(2)
# vib_spindle.markdown('#### 主轴振动信号')
# vib_spindle_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 4])
# # print(smcAC_data)
# c = alt.Chart(vib_spindle_data).mark_line().encode(x='index', y='vib_spindle')
# vib_spindle.altair_chart(c, use_container_width=True)

# vib_table.markdown('#### 台面振动信号')
# vib_table_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 3])
# # print(smcAC_data)
# c = alt.Chart(vib_table_data).mark_line().encode(x='index', y='vib_table')
# vib_table.altair_chart(c, use_container_width=True)
st.markdown('#### 主轴振动信号')
vib_spindle_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 4])
# print(smcAC_data)
c = alt.Chart(vib_spindle_data).mark_line().encode(x='index', y='vib_spindle',color=alt.value("#1f4287"))
st.altair_chart(c, use_container_width=True)

st.markdown('#### 台面振动信号')
vib_table_data = pd.read_excel(path, sheet_name=add_selectbox, usecols=[0, 3])
# print(smcAC_data)
c = alt.Chart(vib_table_data).mark_line().encode(x='index', y='vib_table',color=alt.value("#be6a15"))
st.altair_chart(c, use_container_width=True)
