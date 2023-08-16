import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = r'NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

name_list = ['한림읍', '애월읍', '제주시', '조천읍', '구좌읍', '성산읍', '표선면', '남원읍', '서귀포시',
             '중문', '안덕면', '대정읍', '한경면', '추자도', '우도면']
industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락\(관광\) 및 여가', '요식업', '유흥업소', '운송업']

def categorize_rainfall(rain):
    if rain == 0:
        return '0mm'
    elif rain <= 5:
        return '1~5mm'
    elif rain <= 20:
        return '5~20mm'
    elif rain <= 50:
        return '20~50mm'
    elif rain <= 100:
        return '50~100mm'
    else:
        return '100mm 이상'

rainfall_categories = ['0mm', '1~5mm', '5~20mm', '20~50mm', '50~100mm', '100mm 이상']

def rain():
    # 데이터 로딩
    data_list = []
    for name in name_list:
        filename = f'{name}_filtered_data.csv'
        data = pd.read_csv(filename)
        data['일강수량 정렬'] = data['일강수량'].apply(categorize_rainfall)  # 일강수량을 범주로 변환
        data_list.append(data)

    # 웹 어플리케이션
    st.title('일강수량에 따른 업종별 매출변화')
    option = st.selectbox('원하는 지역을 선택해주세요', name_list)

    # 선택한 지역의 데이터프레임 출력
    st.write(f'{option} 데이터')
    selected_data = data_list[name_list.index(option)]
    st.write(selected_data.head())  # 데이터프레임의 일부분만 보이게 함

    # 일강수량에 따른 업종별 매출 변화 그래프 출력
    st.write(f'{option} - 일강수량에 따른 업종별 매출 변화')
    
    # Sort the data based on custom order
    selected_data['일강수량 정렬'] = pd.Categorical(selected_data['일강수량 정렬'], categories=rainfall_categories, ordered=True)
    selected_data = selected_data.sort_values('일강수량 정렬')
    
    # 평균 매출액 계산
    average_revenues = []
    for industry in industry_list:
        industry_data = selected_data[selected_data['업종_분류'].str.contains(industry)]
        industry_average = industry_data.groupby('일강수량 정렬')['이용금액'].mean() / 1e8
        average_revenues.append(industry_average)

    for industry, industry_average in zip(industry_list, average_revenues):
        st.subheader(f'{option} - {industry}')
        plot_for_industry_r(industry_average, industry)
        
        # 평균 매출 데이터프레임 출력
        st.write(f'{industry}의 평균 매출액 데이터프레임')
        average_revenues_df = pd.DataFrame({
            '일강수량 정렬': industry_average.index,
            '평균 매출액(억)': industry_average.values
        })
        st.dataframe(average_revenues_df, width=800)
        
def plot_for_industry_r(data, industry):
    colors = ['black', 'orange', 'skyblue', 'mediumseagreen', 'yellow', 'blue']
    # 그래프 생성
    fig, ax = plt.subplots()
    ax.bar(data.index, data.values, color=colors)  # 수정된 부분
    ax.set_xlabel('일강수량 정렬', fontproperties=fontprop)
    ax.set_ylabel('평균 매출액(억)', fontproperties=fontprop)
    plt.xticks(fontproperties=fontprop)
    
    # 막대 위에 데이터 레이블 추가
    for i, v in enumerate(data.values):
        ax.text(i, v, f'{v:.2f} 억', ha='center', va='bottom', fontproperties=fontprop, fontsize=8, color='black')

    # Streamlit에 그림 전달
    st.pyplot(fig)
