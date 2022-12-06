## Run this project
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
$ streamlit run main.py
```
