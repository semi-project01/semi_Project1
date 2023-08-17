import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager


font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

def app():
    # cleaned_data.csv 파일 읽기
    df = pd.read_csv('cleaned_data.csv')

    seasonal_avg_revenues = df.groupby(['계절', '업종_분류'])['이용금액'].mean().reset_index()

    # 계절별 업종별 이용금액 평균값 정렬 후 출력
    st.write('## 봄 계절 업종별 이용금액 평균 (오름차순)')
    spring_data = seasonal_avg_revenues[seasonal_avg_revenues['계절'] == '봄']
    spring_data_sorted = spring_data.sort_values('이용금액', ascending=True)
    st.write(spring_data_sorted)

    st.write('## 여름 계절 업종별 이용금액 평균 (오름차순)')
    summer_data = seasonal_avg_revenues[seasonal_avg_revenues['계절'] == '여름']
    summer_data_sorted = summer_data.sort_values('이용금액', ascending=True)
    st.write(summer_data_sorted)

    st.write('## 가을 계절 업종별 이용금액 평균 (오름차순)')
    fall_data = seasonal_avg_revenues[seasonal_avg_revenues['계절'] == '가을']
    fall_data_sorted = fall_data.sort_values('이용금액', ascending=True)
    st.write(fall_data_sorted)

    st.write('## 겨울 계절 업종별 이용금액 평균 (오름차순)')
    winter_data = seasonal_avg_revenues[seasonal_avg_revenues['계절'] == '겨울']
    winter_data_sorted = winter_data.sort_values('이용금액', ascending=True)
    st.write(winter_data_sorted)


# 업종명이 '음식점'이고 지역분류가 'A'인 데이터만 필터링
#food_data = df[(df['업종명'] == '음식점') & (df['지역분류'] == 'A')]

# '음식점'의 이용금액 합계 계산
#total_revenue = food_data['이용금액'].sum()

#golf_data2 = df2[(df2['업종명'] == '골프장 운영업') & (df2['지역_분류'] == '애월읍')]