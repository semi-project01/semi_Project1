#2018풍속&업종별매출	+	2019풍속&업종별매출
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import streamlit as st

def desc02():
    font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
    fontprop = font_manager.FontProperties(fname=font_path, size=10)

    # 데이터 로드
    df = pd.read_csv('cleaned_data.csv')

    # 필요한 열 선택
    selected_columns = ['일자', '최대 풍속', '업종_분류', '이용금액', '최대_풍속_정렬']
    selected_df = df[selected_columns]

    # 일자를 날짜 형식으로 변환
    selected_df['일자'] = pd.to_datetime(selected_df['일자'])

    # 연도별로 데이터 필터링
    selected_df['연도'] = selected_df['일자'].dt.year
    selected_df_2018 = selected_df[selected_df['연도'] == 2018]
    selected_df_2019 = selected_df[selected_df['연도'] == 2019]

    # 업종_분류 기준으로 industry_list에 있는 업종들로 필터링
    industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락(관광) 및 여가', '요식업', '유흥업소', '운송업']

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
    
    # 그래프 생성 함수
    def create_wind_sales_graph(data, year):
        filtered_df = data[data['업종_분류'].isin(industry_list)]
        filtered_df['최대_풍속_정렬'] = filtered_df['최대 풍속'].apply(classify_windspeed)
        windspeed_sales = filtered_df.groupby(['업종_분류', '최대_풍속_정렬'])['이용금액'].mean().reset_index()

        # 1e9로 나누어서 표시
        windspeed_sales['이용금액'] = windspeed_sales['이용금액'] / 1e9
    
        # 바람 범위 순서에 맞게 데이터 정렬
        x_labels = ['고요', '산들바람', '약간강한바람']
        windspeed_sales['최대_풍속_정렬'] = pd.Categorical(windspeed_sales['최대_풍속_정렬'], categories=x_labels, ordered=True)
        windspeed_sales = windspeed_sales.sort_values(['업종_분류', '최대_풍속_정렬'])

        plt.figure(figsize=(12, 8))
        bar_width = 0.09
        colors = ['black', 'orange', 'skyblue', 'mediumseagreen', 'yellow', 'blue', 'chocolate', 'orchid']

        for i, industry in enumerate(industry_list):
            industry_data = windspeed_sales[windspeed_sales['업종_분류'] == industry]
            x = range(len(industry_data['최대_풍속_정렬']))
            bars = plt.bar([pos + (i - (len(industry_list) - 1) / 2) * bar_width for pos in x],
                       industry_data['이용금액'], width=bar_width, label=industry, alpha=0.8, color=colors[i])

            # 막대 위에 숫자값 표시
            for bar in bars:
                height = bar.get_height()
                plt.text(bar.get_x() + bar.get_width() / 2, height,
                         f'{height:.2f}', ha='center', va='bottom', fontproperties=fontprop)

        plt.xticks(x, x_labels, fontproperties=fontprop)

        plt.xlabel('바람 세기', fontproperties=fontprop)
        plt.ylabel('평균 매출액 (10억원)', fontproperties=fontprop)
        plt.legend(prop=fontprop)
        plt.tight_layout()
        plt.show()

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Streamlit 애플리케이션 부분
    st.write("2018년 데이터:")
    create_wind_sales_graph(selected_df_2018, 2018)
    st.pyplot()

    st.write("2019년 데이터:")
    create_wind_sales_graph(selected_df_2019, 2019)
    st.pyplot()