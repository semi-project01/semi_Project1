import streamlit as st
from datetime import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from page import intro as it
from page import se_1 as s1
from page import page_env as penv
from page import manual_page as man
from page import anl_01 as a1
from page import se_3 as s3
from page import anl_02 as a2
from page import anl_03 as a3
from page import anl_04 as a4
from page import anl_05 as a5
from page import anl_06 as a6

item = st.sidebar.selectbox('항목을 골라요.', ['intro','목차', '가상환경 구축 매뉴얼','streamlit 매뉴얼','프로젝트 diagram','조사목적', '분석 01 - 데이터 및 전체 매출 확인','분석 02','분석 03','분석 04','분석 05','분석 06'] )



if item == 'intro':
    it.app()   
elif item == '목차':
    s1.app()   
    # 데이터프레임
    # 그래프 맵
elif item == '가상환경 구축 매뉴얼':
    penv.app()
elif item == 'streamlit 매뉴얼':
    man.app()

# elif item == '프로젝트 diagram':
#     pass
# elif item == '조사 목적':
#     pass
elif item == '분석 01 - 데이터 및 전체 매출 확인':
    a1.app()
elif item == '분석 02':
    a2.app()
elif item == '분석 03':
    a3.app()
elif item == '분석 04':
    a4.app()
elif item == '분석 05':
    a5.app()
elif item == '분석 06':
    a6.app()