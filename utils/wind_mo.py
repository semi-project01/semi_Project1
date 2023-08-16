import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

font_path = r'NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

name_list = ['한림읍', '애월읍', '제주시', '조천읍', '구좌읍', '성산읍', '표선면', '남원읍', '서귀포시',
             '중문', '안덕면', '대정읍', '한경면', '추자도', '우도면']
industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락\(관광\) 및 여가', '요식업', '유흥업소', '운송업']
wind_ranges = [(0, 1), (1, 5), (5, 10), (10, 20)]

def categorize_wind_speed(speed):
    for lower, upper in wind_ranges:
        if lower <= speed < upper:
            return f'{lower}~{upper} m/s'
    return f'{wind_ranges[-1][0]} 이상'

def wind():
    def plot_for_industry_w(data, industry):
        industry_data = data[data['업종_분류'].str.contains(industry)]
    
        # 최대 풍속 구분별로 데이터 추출 및 평균 계산
        average_revenues = []
        for lower, upper in wind_ranges:
            temp_data = industry_data[(industry_data['최대 풍속'] >= lower) & (industry_data['최대 풍속'] < upper)]
            average_revenue = temp_data['이용금액'].mean() / 1e8
            average_revenues.append(average_revenue)
    
        # 그래프 생성
        fig, ax = plt.subplots()
        bars = ax.bar([f'{lower}~{upper} m/s' for lower, upper in wind_ranges], average_revenues)
        ax.set_xlabel('최대 풍속 구분', fontproperties=fontprop)
        ax.set_ylabel('평균 매출액', fontproperties=fontprop)
        plt.xticks(fontproperties=fontprop)
        
        # 데이터 값 표시
        for i, v in enumerate(average_revenues):
            ax.text(bars[i].get_x() + bars[i].get_width() / 2, v, f'{v:.2f} 억', ha='center', va='bottom', fontproperties=fontprop, fontsize=8, color='black')

        ax.set_xlabel('최대 풍속 구분', fontproperties=fontprop)
        ax.set_ylabel('평균 매출액', fontproperties=fontprop)
        plt.xticks(fontproperties=fontprop)

        # Streamlit에 그림 전달
        st.pyplot(fig)

    # 데이터 로딩
    data_list = []
    for name in name_list:
        filename = f'{name}_filtered_data.csv'
        data = pd.read_csv(filename)
        data['최대 풍속 구분'] = data['최대 풍속'].apply(categorize_wind_speed)  # 최대 풍속을 범주로 변환
        data_list.append(data)

    # 웹 어플리케이션
    st.title('최대 풍속에 따른 업종별 매출변화')
    option = st.selectbox('원하는 지역을 선택해주세요', name_list)

    # 선택한 지역의 데이터프레임 출력
    st.write(f'{option} 데이터')
    selected_data = data_list[name_list.index(option)]
    st.write(selected_data.head())  # 데이터프레임의 일부분만 보이게 함

    # 최대 풍속에 따른 업종별 매출 변화 그래프 출력
    st.write(f'{option} - 최대 풍속에 따른 업종별 매출 변화')
    for industry in industry_list:
        st.subheader(f'{option} - {industry}')
        plot_for_industry_w(selected_data, industry)

        # '최대 풍속 구분'에 따른 총 이용금액 평균 계산 (모든 지역 내 업종별)
        pivot_table_each_location = selected_data[selected_data['업종_분류'] == industry].pivot_table(index=['읍면동명', '최대 풍속 구분'], values='이용금액', aggfunc='mean') / 1e8
        st.write(f'모든 지역 - {industry} - 최대 풍속에 따른 총 이용금액 평균')
        st.dataframe(pivot_table_each_location, width=800)
        


