# OpenIE 数控加工中心传感器信号仪表盘<hr>
## 1 Tech Stack
使用 [Streamlit](https://streamlit.io/) Python 3rd Part Lib后端库实现的对机床传感器数据进行处理。<br>
项目使用了conda创建虚拟环境，我们使用的是[miniconda](https://docs.conda.io/en/latest/miniconda.html)按照2中的步骤即可运行本项目。<br>
项目Docker虚拟机正在开发，敬请期待～<br>
特别鸣谢项目其他贡献者：Wang Xiao, Zhang Ziyang, Luo Wenjie, etc.
## 2 Run this project
```bash
$ cd path/to/OpenIE
# create a python virtual environment through miniconda
$ conda create --name openie python=3.8.15
# activate this pyhton env
$ conda activate openie
# use tsinghua source
$ pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# install third part requirements
$ pip install -r requirements.txt
# run this project
$ streamlit run Main_Page.py
```
