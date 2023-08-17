#전체평균기온&업종별매출
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

def desc():
    font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
    fontprop = font_manager.FontProperties(fname=font_path, size=10)

    # 데이터 로드
    df = pd.read_csv('cleaned_data.csv')

    # 필요한 열 선택
    selected_columns = ['일자', '평균 기온', '평균 기온 정렬', '업종_분류', '이용금액']
    selected_df = df[selected_columns]

    # 업종_분류 기준으로 industry_list에 있는 업종들로 필터링
    industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']
    filtered_df = selected_df[selected_df['업종_분류'].isin(industry_list)]

    # 업종_분류별 평균 기온 정렬과 매출 평균 계산
    temperatures_sales = filtered_df.groupby(['업종_분류', '평균 기온 정렬'])['이용금액'].mean().reset_index()

    # 1e9로 나누어서 표시
    temperatures_sales['이용금액'] = temperatures_sales['이용금액'] / 1e8

    # 그래프 생성
    plt.figure(figsize=(12, 8))
    bar_width = 0.09
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightgrey', 'aquamarine', 'orchid', 'chocolate']

    # 그룹화된 바 그래프 생성
    for i, industry in enumerate(industry_list):
        industry_data = temperatures_sales[temperatures_sales['업종_분류'] == industry]
        x = range(len(industry_data['평균 기온 정렬']))
        bars = plt.bar([pos + (i - (len(industry_list) - 1) / 2) * bar_width for pos in x],
                       industry_data['이용금액'], width=bar_width, label=industry, alpha=0.8, color=colors[i])

        # 각 바 위에 값을 표시
        for bar, value in zip(bars, industry_data['이용금액']):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                     f'{value:.2f}', ha='center', va='bottom', fontproperties=fontprop)

    x_labels = ['더위', '무더위', '시원함', '추움']
    x = range(len(x_labels))
    plt.xticks(x, x_labels, fontproperties=fontprop)

    plt.xlabel('평균 기온 구간', fontproperties=fontprop)
    plt.ylabel('평균 매출액 (단위: 1억원)', fontproperties=fontprop)
    plt.legend(prop=fontprop)
    plt.tight_layout()

    st.pyplot(plt)
    def format_currency(amount):
        return f'{amount:.2f} 억'
    temperatures_sales['이용금액(억)'] = temperatures_sales['이용금액'].apply(format_currency)
    st.write("평균 기온 정렬 별 업종별 매출액 데이터")
    st.dataframe(temperatures_sales.set_index('업종_분류')[['평균 기온 정렬', '이용금액(억)']], width=800)
