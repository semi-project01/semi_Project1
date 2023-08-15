import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

from utils import se_3_mo as sm3

def app():
    df = pd.read_csv(r'C:\Users\Seo jeongmu\Documents\python_basic\semi\semi_project1')
    
    st.write(df.head())
    st.write(df.tail())

    df['일자'] = pd.to_datetime(df['일자'])

    # '일자' 열의 연도 추출
    df['연도'] = df['일자'].dt.year

    # 연도별 매출 계산
    annual_sales = df.groupby('연도')['이용금액'].sum()

    # 연도별 매출 데이터 출력
    st.table(annual_sales.reset_index())