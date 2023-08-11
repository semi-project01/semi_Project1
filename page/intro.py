import streamlit as st
import pandas as pd


def app():
    # 제목에 띄어쓰기와 들여쓰기를 적용한 스타일
    st.markdown('<span style="padding-left: 220px; white-space:pre; font-size: 40px; font-weight: bold; color: #1e90ff">2조 퓨처 파이썬</h1>', unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True)
    st.markdown('<span style="padding-left: 120px; white-space:pre; font-size: 50px; font-weight: bold;">제주도 날씨 변화에 따른</span>', unsafe_allow_html=True)
    st.markdown('<span style="padding-left: 0px; white-space:pre; font-size: 50px; font-weight: bold;">업종별 매출의 패턴변화 (2018-2020)</span>', unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

    mem = pd.DataFrame({
        '조원': ['조장', '조원 1', '조원 2'],
        '이름': ['서정무', '김기인', '김영훈']
    }).set_index('조원')


    # 표에 스타일 적용하여 텍스트 크기 조절
    st.write('<style>th, td {font-size: 15px;}</style>', unsafe_allow_html=True)
    st.table(mem)
    