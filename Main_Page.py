import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # 设置屏幕展开方式，宽屏模式布局更好

st.write('## OpenIE 数控机床数据电子仪表盘')
workplan, prop = st.columns(2)

path = './data/mill.xlsx'
workplan_data = pd.read_excel(path, sheet_name='main_data')
workplan.markdown('#### 加工安排')
workplan.write(workplan_data)

prop.markdown('#### 各加工材料占比')
