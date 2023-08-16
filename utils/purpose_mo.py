import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get():
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[주제 및 조사목적]</span>', unsafe_allow_html=True)
    st.write('날씨에 따른 여행객들의 일정과 소비패턴을 WIFI, GPS, Sensor등을 통해 얻어진 데이터를 활용하여 연구된 논문들이 있었습니다.')
    st.write('이를 통해 아이디어를 얻어 대한민국 대표 관광지 중 하나인 제주도로 목표를 설정하고 제주도 날씨 변화에 따른 업종별 매출 패턴 변화를 알아보기 위해서 데이터를 찾아 봤습니다.')
    st.write('그에 따라 저희는 제주도의 지역별 날씨변화에 따른 요식업, 숙박업, 편의시설 등의 업종별 매출 현황을 토대로 데이터를 분석하고 시각화하려고 합니다.')
    st.write('그 결과 날씨에 따라 매출의 변화로 실제 기후가 얼마나 영향을 미치는지 분석을 해보고 날짜별 매출의 변화를 토대로 여행객들이 모이는 시기를 추정하려고 합니다.')
    st.image('./image/purpose.png', use_column_width=True)
    
    