import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc


font_path = 'C:/Windows/Fonts/NanumGothic.ttf'  # 해당 경로는 실제 설치된 폰트 경로로 변경해주세요
# 폰트 이름 얻기
font_name = font_manager.FontProperties(fname=font_path).get_name()
# Matplotlib 설정 변경
rc('font', family=font_name)

#연간 총 매출량 체크
def total_check1():
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[제주도 연도별 총 매출 차이] </span>', unsafe_allow_html=True)  
    df = pd.read_csv('./cleaned_data.csv')
    df['일자'] = pd.to_datetime(df['일자'])
    # '일자' 열의 연도 추출
    df['연도'] = df['일자'].dt.year
    # 연도별 매출 계산
    annual_sales = df.groupby('연도')['이용금액'].sum()

    # 단위를 조로 변환하는 함수 정의
    def format_trillions(x):
        return f'{x/1e12:,.2f} 조'

    # 연도별 매출 데이터의 단위를 조로 변경
    annual_sales_formatted = annual_sales.apply(format_trillions)

    st.dataframe(annual_sales_formatted)

    # '일자' 열을 datetime 형식으로 변환

    # 연도별 매출량 계산
    annual_sales = df.groupby('연도')['이용금액'].sum() / 1e12  # 단위를 1조(조)로 변경

   # Streamlit 애플리케이션 시작
   # st.header('연도별 매출량 비교')

    # 각 연도별 색상 설정
    colors = ['skyblue', 'lightgreen', 'lightcoral']

    # 막대그래프 그리기
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = plt.bar(annual_sales.index, annual_sales, color=colors)
    plt.xlabel('연도')
    plt.ylabel('이용금액 (단위: 조)')
    plt.xticks(annual_sales.index)

    # 막대 위에 데이터 값을 표시
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', color='black', fontsize=10)

    plt.tight_layout()

    # Matplotlib 그래프를 Streamlit에 표시
    st.pyplot(fig)

#분기별 매출 변화
def total_check2():
    st.markdown('<span style= "font-size: 20px; font-weight: bold;">[제주도 분기별 매출 차이] </span>', unsafe_allow_html=True)  
    df = pd.read_csv('./cleaned_data.csv')
    # '일자' 열을 datetime 형식으로 변환
    df['일자'] = pd.to_datetime(df['일자'])

    # '일자' 열을 기준으로 '분기' 열 생성
    df['분기'] = df['일자'].dt.to_period('Q')

    # 분기별 총 이용금액 계산 및 단위 변경 (조 단위로)
    quarterly_total_sales = df.groupby('분기')['이용금액'].sum() / 1e12  # 단위를 '조'으로 변경

    #st.dataframe(quarterly_total_sales)

    # 단위를 조로 변환하는 함수 정의
    def format_trillions(x):
        return f'{x/1e12:,.2f} 조'

    # 시각화: 분기별 총 이용금액 비교
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']  # 원하는 색상 추가
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = plt.bar(quarterly_total_sales.index.astype(str), quarterly_total_sales, color=colors)
    plt.title('분기별 총 매출액 비교')
    plt.xlabel('분기')
    plt.ylabel('총 이용금액 (단위: 조)')
    plt.xticks(rotation=45)

    # 막대 위에 데이터 값을 표시 (소수점 2자리까지 표시)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', color='black', fontsize=10)

    plt.tight_layout()
    # Matplotlib 그래프를 Streamlit에 표시
    st.pyplot(fig)

# 연도 및 계절별 매출 변화
def total_check3():
    st.markdown('<span style="font-size: 20px; font-weight: bold;">[제주도 계절별 매출 차이] </span>', unsafe_allow_html=True)
    df = pd.read_csv('./cleaned_data.csv')
    # '일자' 열을 datetime 형식으로 변환
    df['일자'] = pd.to_datetime(df['일자'])

    # '일자' 열을 기준으로 '분기' 열 생성
    df['연도_계절'] = df['일자'].dt.year.astype(str) + ' ' + df['계절']

    # 연도별 계절별 계산 및 단위 변경 (조 단위로)
    annual_seasonal_sales = df.groupby('연도_계절')['이용금액'].sum() / 1e12

    seasons = ['2018 봄', '2018 여름', '2018 가을', '2018 겨울',
               '2019 봄', '2019 여름', '2019 가을', '2019 겨울',
               '2020 봄', '2020 겨울']
    annual_seasonal_sales = annual_seasonal_sales.reindex(seasons)

    # 단위를 조로 변환하는 함수 정의
    def format_trillions(x):
        return f'{x:.2f} 조'

    # 시각화: 분기별 총 이용금액 비교
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']  # 각 계절별 색상 설정
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(annual_seasonal_sales.index, annual_seasonal_sales, color=colors)

    #ax = annual_seasonal_sales.plot(kind='bar', color='skyblue')
    plt.title('연도별 계절별 매출량 비교')
    plt.xlabel('연도-계절')
    plt.ylabel('이용금액')
    plt.xticks(rotation=45)

    # 막대 위에 수치 표시
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{format_trillions(yval)}', ha='center', va='bottom', color='black', fontsize=10)

    plt.tight_layout()

    # Matplotlib 그래프를 Streamlit에 표시
    st.pyplot(fig)
