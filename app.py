import streamlit as st
from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from page import intro as it
from page import se_1 as s1
from page import se_2 as s2
from page import se_3 as s3
from page import page_env as penv
from page import manual_page as man


item = st.sidebar.selectbox('항목을 골라요.', ['intro','목차', '가상환경','streamlit manual','선택3',] )



if item == 'intro':
    it.app()   
elif item == '목차':
    s1.app()   
    # 데이터프레임
    # 그래프 맵
elif item == '가상환경':
    penv.app()
elif item == 'streamlit manual':
    man.app()

elif item == '선택3':
    s3.app()
    # streamlit_folium