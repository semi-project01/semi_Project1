#전체강수량&업종별매출
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

def desc():
    font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
    fontprop = font_manager.FontProperties(fname=font_path, size=10)

    df = pd.read_csv('cleaned_data.csv')
    selected_columns = ['일자', '일강수량', '업종_분류', '이용금액']
    selected_df = df[selected_columns]
    selected_df = selected_df.copy()
    selected_df['일자'] = pd.to_datetime(selected_df['일자'])

    # 업종_분류 기준으로 industry_list에 있는 업종들로 필터링
    industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']
    filtered_df = selected_df[selected_df['업종_분류'].isin(industry_list)]

    # 강수량 범위 분류 함수
    def classify_rainfall(rain):
        if rain < 5:
            return '매우 약한 강수'
        elif rain < 20:
            return '약한 강수'
        elif rain < 50:
            return '보통의 강수'
        elif rain < 100:
            return '강한 강수'
        else:
            return '매우 강한 강수'

    # 강수량 범위 분류 열 추가
    filtered_df['강수량_범위'] = filtered_df['일강수량'].apply(classify_rainfall)
    
    # 업종_분류별 강수량 범위와 매출 평균 계산
    rainfall_sales = filtered_df.groupby(['업종_분류', '강수량_범위'])['이용금액'].mean().reset_index()

    # 1e9로 나누어서 표시
    rainfall_sales['이용금액'] = rainfall_sales['이용금액'] / 1e9
    
    # 그래프 생성
    plt.figure(figsize=(12, 8))
    bar_width = 0.09
    colors = ['black', 'orange', 'skyblue', 'mediumseagreen', 'yellow', 'blue', 'chocolate', 'orchid']
    
    # 그룹화된 바 그래프 생성    
    for i, industry in enumerate(industry_list):
        industry_data = rainfall_sales[rainfall_sales['업종_분류'] == industry]
        x = range(len(industry_data['강수량_범위']))
        bars = plt.bar([pos + (i - (len(industry_list) - 1) / 2) * bar_width for pos in x],
                       industry_data['이용금액'], width=bar_width, label=industry, alpha=0.8, color=colors[i])

    # 각 바 위에 값을 표시
        for bar, value in zip(bars, industry_data['이용금액']):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                     f'{value:.2f}', ha='center', va='bottom', fontproperties=fontprop)
            
        x_labels = ['매우 약한 강수', '약한 강수', '보통의 강수', '강한 강수', '매우 강한 강수']
        rainfall_sales['강수량_범위'] = pd.Categorical(rainfall_sales['강수량_범위'], categories=x_labels, ordered=True)
        rainfall_sales = rainfall_sales.sort_values(['업종_분류', '강수량_범위'])
            
        x_labels = ['매우 약한 강수', '약한 강수', '보통의 강수', '강한 강수', '매우 강한 강수']
        x = range(len(x_labels))
        plt.xticks(x, x_labels, fontproperties=fontprop)
        
        plt.xlabel('강수량 범위 (단위: 10억원)', fontproperties=fontprop)
        plt.ylabel('평균 매출액', fontproperties=fontprop)
        plt.legend(prop=fontprop)
        plt.tight_layout()
        
    st.pyplot(plt)
