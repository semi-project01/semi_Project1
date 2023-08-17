import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import seaborn as sns

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']

def result():
    def plot_for_industry_t(data, industry):
        industry_data = data[data['업종_분류'] == industry]  # 업종명 필터링

        # 계절별로 데이터 추출 및 평균 계산
        season_labels = ['봄', '여름', '가을', '겨울']
        season_revenues = []
        for label in season_labels:
            season_data = industry_data[industry_data['계절'] == label]
            average_revenue = season_data['이용금액'].mean() / 1e8  # 억 원 단위로 변환
            season_revenues.append(average_revenue)

        # 데이터프레임 생성
        season_df = pd.DataFrame({
            '계절': season_labels,
            '평균 매출액 (억 원)': season_revenues
        })

        st.write(f'{industry}에 대한 데이터프레임')
        st.write(season_df)

        # 그래프 생성
        plt.figure(figsize=(10, 6))

        # 막대 그래프 그리기
        colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']  # 각 계절별 색상 설정
        sns.barplot(x='계절', y='평균 매출액 (억 원)', data=season_df, palette=colors)

        # 막대 위에 데이터 값을 표시
        ax = plt.gca()  # 현재 axes 가져오기
        for bar in ax.patches:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', color='black', fontsize=10)

        # 그래프 제목 및 축 레이블 설정
        plt.title(f'{industry} 평균 매출 변화')
        plt.xlabel('계절')
        plt.ylabel('평균 매출액 (억 원)')

        st.pyplot()

    # 데이터 로딩
    data_path = 'cleaned_data.csv'
    data = pd.read_csv(data_path)

    # 웹 어플리케이션
    st.title('[결론]')

    # 선택한 업종별로 그래프 생성
    for industry in industry_list:
        st.subheader(f'{industry} - 계절별 평균 매출액 데이터')
        plot_for_industry_t(data, industry)




    st.header('[최종 결론]')
    st.subheader('여름 : 제주도 방문객에게 추천하는 업종')
    st.image('./image/result01.png', use_column_width=True)
    st.write('> 여름에는 숙박, 요식업, 운송업이 매출이 높습니다')

    st.subheader('가을 : 제주도 방문객에게 추천하는 업종')
    st.image('./image/result02.png', use_column_width=True)
    st.write('> 가을에는 골프장, 스포츠, 오락관광 및 여가, 소매업이 매출이 높습니다')

    st.write('1. 계절에 따른 업종별 평균 매출 변화를 분석하여 날씨의 유의미한 영향을 확인하여 각 업종별로 가장 높은 매출을 기록한 계절을 확인 가능')

    st.write('2. 분석 결과물들을 통해 수많은 관광객들의 각자의 목적에 맞는 여행 시기를 설정하는데 도움을 줄 수 있음')

    st.write('3. 이외의 여행 목적에 따른 지역추천에 대한 분석은 데이터수집에 어려움이 있어 문제해결에 어려움이 있음')

