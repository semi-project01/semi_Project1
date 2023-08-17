import streamlit as st
from page import intro as it
from page import se_1 as s1
from page import page_env as penv
from page import manual_page as man
from page import purpose as pu
from page import anl_01 as a1
from page import anl_02 as a2
from page import anl_03 as a3
from page import anl_04 as a4
from page import anl_05 as a5
from page import anl_06 as a6
from page import rain_page as a7
from page import wind_page as a8
from page import diagram as di
from page import seaseon as se
from page import result_page as re
item_name = ['intro','목차', '가상환경 구축 매뉴얼','streamlit 매뉴얼','프로젝트 diagram','조사 목적', 
              '분석 01 - 데이터 및 전체 매출 확인',
              '분석 02 - 연도별 날씨 변화',
              '분석 03 - 강수량 및 업종별 매출 비교',
              '분석 04 - 풍속 및 업종별 매출 비교',
              '분석 05 - 기온 및 업종별 매출 비교',
              '분석 06 - 기온에 따른 업종별 매출 변화',
              '분석 07 - 강수량에 따른 업종별 매출 변화',
              '분석 08 - 풍속에 따른 업종별 매출 변화',
              '분석 09 - 계절에 따른 업종별 매출 변화',
              '결론'
              ]
item = st.sidebar.selectbox('항목을 고르세요.', item_name)

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

elif item == '프로젝트 diagram':
    di.app()
elif item == '조사 목적':
    pu.app()
elif item == '분석 01 - 데이터 및 전체 매출 확인':
    a1.app()
elif item == '분석 02 - 연도별 날씨 변화':
    a2.app()
elif item == '분석 03 - 강수량 및 업종별 매출 비교':
    a3.app()
elif item == '분석 04 - 풍속 및 업종별 매출 비교':
    a4.app()
elif item == '분석 05 - 기온 및 업종별 매출 비교':
    a5.app()
elif item == '분석 06 - 기온에 따른 업종별 매출 변화':
    a6.app()
elif item == '분석 07 - 강수량에 따른 업종별 매출 변화':
    a7.app()
elif item == '분석 08 - 풍속에 따른 업종별 매출 변화':
    a8.app()
elif item == '분석 09 - 계절에 따른 업종별 매출 변화':
    se.app()
elif item == '결론':
    re.app()