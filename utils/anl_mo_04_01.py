#전체최대풍속 업종별 그래프
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

def desc():
    font_path = r'NanumGothic.ttf'
    fontprop = font_manager.FontProperties(fname=font_path, size=10)

    # 데이터 로드
    df = pd.read_csv('cleaned_data.csv')

    # 필요한 열 선택
    selected_columns = ['일자', '최대 풍속', '업종_분류', '이용금액', '최대_풍속_정렬']
    selected_df = df[selected_columns]

    # 바람 세기 분류 함수
    def classify_windspeed(wind):
        if wind < 1:
            return '고요'
        elif wind < 5:
            return '산들바람'
        elif wind < 10:
            return '약간강한바람'
        elif wind < 20:
            return '강한바람'
        else:
            return '매우강한바람'

    # 바람 세기 범위 분류 열 추가
    selected_df['최대_풍속_정렬'] = selected_df['최대 풍속'].apply(classify_windspeed)

    # 업종_분류 기준으로 industry_list에 있는 업종들로 필터링
    industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']
    filtered_df = selected_df[selected_df['업종_분류'].isin(industry_list)]

    # 업종_분류별 바람 세기 범위와 매출 평균 계산
    windspeed_sales = filtered_df.groupby(['업종_분류', '최대_풍속_정렬'])['이용금액'].mean().reset_index()

    # 1e9로 나누어서 표시
    windspeed_sales['이용금액'] = windspeed_sales['이용금액'] / 1e9

    # 그래프 생성
    plt.figure(figsize=(12, 8))
    bar_width = 0.09
    colors = ['black', 'orange', 'skyblue', 'mediumseagreen', 'yellow', 'blue', 'chocolate', 'orchid']

    # 그룹화된 바 그래프 생성
    for i, industry in enumerate(industry_list):
        industry_data = windspeed_sales[windspeed_sales['업종_분류'] == industry]
        x = range(len(industry_data['최대_풍속_정렬']))
        bars = plt.bar([pos + (i - (len(industry_list) - 1) / 2) * bar_width for pos in x],
                       industry_data['이용금액'], width=bar_width, label=industry, alpha=0.8, color=colors[i])

        # 각 바 위에 값을 표시
        for bar, value in zip(bars, industry_data['이용금액']):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                     f'{value:.2f}', ha='center', va='bottom', fontproperties=fontprop)

    x_labels = ['고요', '산들바람', '약간강한바람', '강한바람', '매우강한바람']
    x = range(len(x_labels))
    plt.xticks(x, x_labels, fontproperties=fontprop)

    plt.xlabel('바람 세기 범위', fontproperties=fontprop)
    plt.ylabel('평균 매출액 (단위: 10억원)', fontproperties=fontprop)
    plt.legend(prop=fontprop)
    plt.tight_layout()
    
    # 그래프 출력
    st.pyplot(plt)
