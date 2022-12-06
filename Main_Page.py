import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # 设置屏幕展开方式，宽屏模式布局更好

st.write('## OpenIE 数控机床数据电子仪表盘')
workplan, time, frequency = st.columns(3)

path = './data/mill.xlsx'
workplan_data = pd.read_excel(path, sheet_name='main_data')
workplan.markdown('#### 加工安排')
workplan.write(workplan_data)

time.markdown('#### 时域特征')
time.write('''
$ 绝对均值：|\\bar{x}|=\\frac{1}{N} \\sum_{i=1}^{N}\left|x_{i}\\right| $ \n
$ 峰值：x_{pesk}=X_{max} $ \n
$ 均方根值：x_{rms}=\sqrt{\\frac{1}{N} \sum_{k=1}^{N} x_{i}^{2}} $ \n
$ 方根幅值：x_{kurtosis}=\\frac{1}{N} \sum_{k=1}^{N}(\pi)^{n} $ \n
$ 峭度值：x_{ra}=\left(\\frac{1}{N} \sum_{i=1}^{N} \sqrt{|x_i|}\\right)^{2} $ \n
$ 波形因子：f_{shape}=\\frac{x_{rms}}{|\\bar{x}|} $ \n
$ 脉冲因子：f_{pulse}=\\frac{x_{peak}}{|x|} $ \n
$ 峰值因子：f_{crest}=\\frac{x_{peak}}{x_{rms}} $ \n
$ 裕度因子：f_{celearance}=\\frac{x_{peak}}{x_{ra}} $ \n
''')

frequency.markdown('#### 频域特征')
frequency.write('''
$ 重心频率：F_{FC}=\\frac{\int_{0}^{+\infty}f(t)FFT(t)dt}{\int_{0}^{+\infty} FFT(t)dt} $ \n
$ 均方频率：F_{MSF}=\\frac{\int_{0}^{+\infty} FFT(t)f(t)^{2}dt}{\int_{0}^{+\infty}FFT(t)dt} $ \n
$ 均方根频率：F_{RMSF}=\sqrt{\\frac{\int_{0}^{+\infty}FFT(t)f(t)^{2}dt}{\int_{0}^{+\infty}FFT(t)dt}} $ \n
$ 频率方差：F_{VF}=\\frac{\int_{0}^{+\infty}(f(t)-\\frac{\int_{0}^{+\infty}f(t)FFT(t)dt}{\int_{0}^{+\infty}FFT(t)dt} )^{2}dt}{\int_{0}^{+\infty}FFT(t)dt} $ \n
$ \  $ \n
''')
frequency.markdown('#### 时频域特征')
frequency.write('''
$ 小波包分析 $ \n
''')
st.write('''
## 说明：
本网站功能是对CNC机床传感器数据进行数据分析以及信号图像可视化，项目源码可在[QianZehao's OpenIE Repository](https://gitee.com/qian_zehao/OpenIE)中获取。 \n
Current、Vibration、AE页面是对机床主轴交流/直流电压信号，主轴/台面的振动和噪声信号进行交互式可视化。
''')