#2018강수량&업종별매출	+	2019강수량&업종별매출
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

df = pd.read_csv('cleaned_data.csv')
selected_columns = ['일자', '일강수량', '업종_분류', '이용금액']
selected_df = df[selected_columns]

# 일자를 날짜 형식으로 변환
selected_df['일자'] = pd.to_datetime(selected_df['일자'])
# 연도별로 데이터 필터링
selected_df['연도'] = selected_df['일자'].dt.year
selected_df_2018 = selected_df[selected_df['연도'] == 2018]
selected_df_2019 = selected_df[selected_df['연도'] == 2019]
# 업종_분류 기준으로 industry_list에 있는 업종들로 필터링
industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']

# 강수량 범위 분류
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
    
# 그래프 생성 쪽
def create_rainfall_sales_graph(data, year):
    filtered_df = data[data['업종_분류'].isin(industry_list)]
    filtered_df['강수량_범위'] = filtered_df['일강수량'].apply(classify_rainfall)
    rainfall_sales = filtered_df.groupby(['업종_분류', '강수량_범위'])['이용금액'].mean().reset_index()
    
    # 1e8로 나누어서 표시
    rainfall_sales['이용금액'] = rainfall_sales['이용금액'] / 1e8

    # 강수량 범위 순서에 맞게 데이터 정렬
    x_labels = ['매우 약한 강수', '약한 강수', '보통의 강수', '강한 강수', '매우 강한 강수']
    rainfall_sales['강수량_범위'] = pd.Categorical(rainfall_sales['강수량_범위'], categories=x_labels, ordered=True)
    rainfall_sales = rainfall_sales.sort_values(['업종_분류', '강수량_범위'])
    
    plt.figure(figsize=(12, 8))
    bar_width = 0.09
    colors = ['black', 'orange', 'skyblue', 'mediumseagreen', 'yellow', 'blue', 'chocolate', 'orchid']
        
    for i, industry in enumerate(industry_list):
        industry_data = rainfall_sales[rainfall_sales['업종_분류'] == industry]
        x = range(len(industry_data['강수량_범위']))
        bars = plt.bar([pos + (i - (len(industry_list) - 1) / 2) * bar_width for pos in x],
                           industry_data['이용금액'], width=bar_width, label=industry, alpha=0.8, color=colors[i])

        # 막대 위에 숫자값 표시
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                     f'{height:.2f}', ha='center', va='bottom', fontproperties=fontprop)

    plt.xticks(x, x_labels, fontproperties=fontprop)
    plt.xlabel('강수량 범위', fontproperties=fontprop)
    plt.ylabel('평균 매출액 (단위 : 억)', fontproperties=fontprop)
    plt.legend(prop=fontprop)
    plt.tight_layout()
    return rainfall_sales

def desc02():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Streamlit 애플리케이션 부분
    st.write("2018년 데이터")
    create_rainfall_sales_graph(selected_df_2018, 2018)
    st.pyplot()
    st.write("2018년 데이터 표")
    st.dataframe(selected_df_2018.set_index('일자')[['일강수량', '업종_분류', '이용금액']], width=800)

    st.write("2019년 데이터")
    create_rainfall_sales_graph(selected_df_2019, 2019)
    st.pyplot()
    st.write("2019년 데이터 표")
    st.dataframe(selected_df_2019.set_index('일자')[['일강수량', '업종_분류', '이용금액']], width=800)
