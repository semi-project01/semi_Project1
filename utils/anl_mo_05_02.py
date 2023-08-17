#2018평균기온&업종별매출	+	2019평균기온&업종별매출
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

df = pd.read_csv('cleaned_data.csv')
selected_columns = ['일자', '평균 기온', '업종_분류', '이용금액', '평균 기온 정렬']
selected_df = df[selected_columns]

# 일자를 날짜 형식으로 변환
selected_df['일자'] = pd.to_datetime(selected_df['일자'])
# 연도별로 데이터 필터링
selected_df['연도'] = selected_df['일자'].dt.year
selected_df_2018 = selected_df[selected_df['연도'] == 2018]
selected_df_2019 = selected_df[selected_df['연도'] == 2019]
# 업종_분류 기준으로 industry_list에 있는 업종들로 필터링
industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']

# 그래프 생성쪽
def create_temper_sales_graph(data, year):
    filtered_df = data[data['업종_분류'].isin(industry_list)]
    
    temperature_sales = filtered_df.groupby(['업종_분류', '평균 기온 정렬'])['이용금액'].mean().reset_index()
    temperature_sales['이용금액'] /= 1e8

    x_labels = ['더위', '무더위', '시원함', '추움']
    temperature_sales['평균 기온 정렬'] = pd.Categorical(temperature_sales['평균 기온 정렬'], categories=x_labels, ordered=True)
    temperature_sales = temperature_sales.sort_values(['업종_분류', '평균 기온 정렬'])
        
    plt.figure(figsize=(12, 8))
    bar_width = 0.09
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightgrey', 'aquamarine', 'orchid', 'chocolate']

    for i, industry in enumerate(industry_list):
        industry_data = temperature_sales[temperature_sales['업종_분류'] == industry]
        x = range(len(industry_data['평균 기온 정렬']))
        bars = plt.bar([pos + (i - (len(industry_list) - 1) / 2) * bar_width for pos in x],
                       industry_data['이용금액'], width=bar_width, label=industry, alpha=0.8, color=colors[i])

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height,
                     f'{height:.2f}', ha='center', va='bottom', fontproperties=fontprop)

    plt.xticks(x, x_labels, fontproperties=fontprop)

    plt.xlabel('기온 범위', fontproperties=fontprop)
    plt.ylabel('평균 매출액 (단위: 1억원)', fontproperties=fontprop)
    plt.legend(prop=fontprop)
    plt.tight_layout()

def desc02():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write("2018년 데이터:")
    create_temper_sales_graph(selected_df_2018, 2018)
    st.pyplot()
    st.write("2018년 데이터 표")
    avg_temper_sales_2018 = selected_df_2018[selected_df_2018['업종_분류'].isin(industry_list)].groupby(['업종_분류', '평균 기온 정렬'])['이용금액'].mean().reset_index()
    avg_temper_sales_2018['이용금액'] /= 1e8
    st.dataframe(avg_temper_sales_2018, width=800)

    st.write("2019년 데이터:")
    create_temper_sales_graph(selected_df_2019, 2019)
    st.pyplot()
    st.write("2019년 데이터 표")
    avg_temper_sales_2019 = selected_df_2019[selected_df_2019['업종_분류'].isin(industry_list)].groupby(['업종_분류', '평균 기온 정렬'])['이용금액'].mean().reset_index()
    avg_temper_sales_2019['이용금액'] /= 1e8
    st.dataframe(avg_temper_sales_2019, width=800)
