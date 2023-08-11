import streamlit as st
import pandas as pd
from utils import se_1_mo as sm1


def app():
    st.title("2조 :blue[퓨처 파이썬]")

    mem = pd.DataFrame({
        'index': ['조장', '조원 1', '조원 2'],
        'column': ['서정무', '김기인', '김영훈']
    })

    st.write(mem)

    st.header(f'주제: 제주도 날씨 변화에 따른 업종별 매출의 패턴변화 (2018-2020)')


    st.subheader('I N D E X')
    
    st.write('1. 가상환경 구축 매뉴얼')
    st.write('2. streamlit 매뉴얼')
    st.write('3. 프로젝트 diagram')
    st.write('4. 처리 및 분석한 내용')