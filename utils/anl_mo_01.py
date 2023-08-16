import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc


def total_check():      
    df = pd.read_csv('./jeju_data.csv', sep=',', encoding='euc-kr')
    
    st.write('데이터 값을 확인해보겠습니다.')
    st.write(df.head())
    st.write(df.tail())
    st.markdown('<span style="padding-left: 240px; white-space:pre; font-size: 20px; font-weight: bold;">-csv 데이터 형태-</span>', unsafe_allow_html=True)
    #st.write('csv 데이터 형태입니다.')

    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[데이터 모양과 크기 확인]</span>', unsafe_allow_html=True)
    st.write(df.shape)
    st.write('-- 1603367행, 9열 구성 확인')

    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[데이터프레인 내용 확인]</span>', unsafe_allow_html=True)
    st.dataframe(df.info())
    
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[데이터프레임의 기술 통계 정보 확인]</span>', unsafe_allow_html=True)
    st.write(df.describe())

    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[각 열별 누락된 값 확인]</span>', unsafe_allow_html=True)
    st.write(df.isnull().sum())

    st.markdown('----')
  
def sort_data():
    st.markdown('<span style= "font-size: 40px; font-weight: bold;">[데이터 분류 작업]</span>', unsafe_allow_html=True)
    st.markdown('- 먼저 많이 세분화 되어 있는 지역, 업종, 일자, 기온, 풍속들을 일정한 데이터에 맞춰 분석하기 쉽게 분류를 하여 새롭게 열을 추가하 였습니다.')

    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[업종별 분류]- 총 42개 업종 정리</span>', unsafe_allow_html=True)  
    st.write('''
        1. 골프장_운영업 = ['골프장 운영업']

        2. 소매업 = ['관광 민예품 및 선물용품 소매업', '슈퍼마켓', '그외 기타 종합 소매업','건강보조식품 소매업','화장품 및 방향제 소매업', '과실 및 채소 소매업','체인화 편의점','기타 대형 종합 소매업','수산물 소매업',
        '빵 및 과자류 소매업', '육류 소매업', '면세점' , '차량용 주유소 운영업','차량용 가스 충전업']

        3. 스포츠_관련_업종 =['스포츠 및 레크레이션 용품 임대업','그외 기타 스포츠시설 운영업','기타음식료품위주종합소매업']

        4. 숙박업 = ['여관업', '호텔업','휴양콘도 운영업']

        5. 관광업종 = ['욕탕업', '그외 기타 분류안된 오락관련 서비스업', '마사지업','기타 갬블링 및 베팅업','전시 및 행사 대행업', '여행사업', '자동차 임대업','기타 수상오락 서비스업']

        6. 요식업종 = ['피자, 햄버거, 샌드위치 및 유사 음식점업','서양식 음식점업','일식 음식점업', '한식 음식점업','중식 음식점업', '기타 외국식 음식점업']

        7. 유흥업소 = ['일반유흥 주점업','비알콜 음료점업', '기타 주점업']

        8. 운송업 = ['택시 운송업', '내항 여객 운송업', '정기 항공 운송업', '버스 운송업']
        ''')
    
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[지역 분류]- 총 43개 지역 정리</span>', unsafe_allow_html=True)  
    image_path = './image/jeju_area.png'

    # 이미지 표시
    st.image(image_path, caption='이미지 캡션', use_column_width=True)
    st.write('''
        한림읍 = ['한림읍']
             
        애월읍 = ['애월읍']
             
        제주시 = ['오라동', '도두동', '봉개동', '이도1동', '이도2동', '외도동', '화북동', '일도1동', '일도2동', '삼양동', '용담1동', '용담2동', '건압동', '노형동', '아라동', '이호동', '삼도1동', '삼도2동', '연동','건입동']
             
        조천읍 = ['조천읍']
             
        구좌읍 = ['구좌읍']
             
        성산읍 = ['성산읍']
             
        표선면 = ['표선면']
             
        남원읍 = ['남원읍']
             
        서귀포시 = ['서홍동', '정방동', '송산동', '대륜동', '효돈동', '천지동', '대천동', '동홍동', '중앙동']
             
        중문 = ['예래동', '중문동']
             
        안덕면 = ['안덕면']
             
        대정읍 = ['대정읍']
             
        한경면 = ['한경면']
             
        추자도  = ['추자면']
             
        우도면  = ['우도면']
        ''')
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[계절 분류]- 봄, 여름, 가을, 겨울 구분</span>', unsafe_allow_html=True)  
    st.write('''
        봄  : 3 ~ 5월
            
        여름 : 6 ~ 8월
            
        가을 : 9 ~ 11월

        겨울 : 12 ~ 2월
        ''')
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[평균 기온에 따른 날씨 분류] </span>', unsafe_allow_html=True)  
    st.write('''
        무더위 : 30도 이상
            
        더위 : 20도 ~ 30도 미만
            
        시원함 : 10도 ~ 20도 미만

        추움 : 10도 미만
        ''')
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[최대 풍속 분류] </span>', unsafe_allow_html=True)  
    st.write('''
        바람이 거의 없음 (Calm) : 0 ~ 5 m/s
            
        약간 강한 바람 (Gentle Breeze) : 5 ~ 10 m/s 
            
        강한 바람 (Moderate Breeze) : 10 ~ 20 m/s 

        매우 강한 바람 (Strong Breeze) : 20 ~ 29  m/s
             
        폭풍 (Storm) : 29  m/s 이상
        ''')

    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[새로운 CSV파일로 저장 후 열 확인] </span>', unsafe_allow_html=True)  
    df = pd.read_csv('./sort_new_jeju.csv')
    st.write(df.head())
    st.write(df.tail())
    st.markdown('----')