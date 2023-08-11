import streamlit as st
import pandas as pd


def app():

    # CSS 스타일 적용을 위한 HTML 태그 사용
    # 마크다운 스타일로 줄 긋기
    
    st.markdown(
        #'<span style="padding-left: 200px;; font-size: 70px; font-weight: bold; color: #1e90ff">•</span>'
        '<span style="padding-left: 150px; white-space:pre; font-size: 70px; font-weight: bold; color: #1e90ff">•    I N D E X    •</span>', unsafe_allow_html=True)
    st.markdown('----')
    st.markdown('<p style="font-size: 30px; font-weight: 650;">1. 가상환경 구축 매뉴얼</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 30px; font-weight: 650;">2. Streamlit 사용 메뉴얼</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 30px; font-weight: 650;">3. 프로젝트 diagram</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 30px; font-weight: 650;">4. 처리 및 분석한 내용</p>', unsafe_allow_html=True)

    