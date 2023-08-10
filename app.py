import streamlit as st
from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from page import se_1 as s1
from page import se_2 as s2
from page import se_3 as s3


todays = dt.today()
tod = todays.strftime(' %Y년 %m월 %d일')
st.title(f'{tod}')
st.header(f'개인적인 복습입니다. 가상환경 구축하기')

st.subheader('오늘은 세미프로젝트 진행전 작업구조 만들기입니다.')

st.write('만들어봅시다.')

item = st.sidebar.selectbox('항목을 골라요.',  ['선택1', '선택2','선택3'] )


if item == '선택1':
    s1.app()   
    # 데이터프레임
    # 그래프 맵
elif item == '선택2':
    s2.app2()
    # text input과 button

elif item == '선택3':
    s3.app()
    # streamlit_folium