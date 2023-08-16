import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import seaborn as sns

font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname=font_path, size=10)

name_list = ['한림읍', '애월읍', '제주시', '조천읍', '구좌읍', '성산읍', '표선면', '남원읍', '서귀포시',
             '중문', '안덕면', '대정읍', '한경면', '추자도', '우도면']
industry_list = ['골프장 운영업', '소매업', '숙박업', '스포츠 관련 업종', '오락\(관광\) 및 여가', '요식업', '유흥업소', '운송업']

# def tem_():
#     def plot_for_industry_t(data, industry):
#         industry_data = data[data['업종_분류'].str.contains(industry)]
    
#         # 평균 기온 구분별로 데이터 추출 및 평균 계산
#         temp_labels = ['시원함', '더위', '무더위', '추움']
#         average_revenues = []
#         for label in temp_labels:
#             temp_data = industry_data[industry_data['평균 기온 정렬'] == label]
#             average_revenue = temp_data['이용금액'].mean() / 1e8  # 단위를 억 원으로 변경
#             average_revenues.append(average_revenue)

#         # # 선택한 지역의 업종별 매출 데이터 추출
#         # selected_industry_data = selected_data[selected_data['업종명'].isin(industry_list)]
#         # selected_industry_data = selected_industry_data.groupby(['업종명', '평균 기온 정렬'])['이용금액'].mean() / 1e8  # 억 원 단위로 변환
#         # selected_industry_data = selected_industry_data.reset_index()

#         # # '평균 기온 정렬' 열의 순서 변경
#         # selected_industry_data['평균 기온 정렬'] = pd.Categorical(selected_industry_data['평균 기온 정렬'], 
#         #                                                       categories=['시원함', '더위', '무더위', '추움'], 
#         #                                                       ordered=True)
#         # selected_industry_data = selected_industry_data.sort_values('평균 기온 정렬')
#         # st.write(selected_industry_data)

#         # 그래프 생성
#         plt.ylabel('평균 매출액 (억 원)')
#         plt.figure(figsize=(10, 6))
#         ax = plt.gca()  # 현재 axes 가져오기
#         colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']  # 각 계절별 색상 설정
#         bars = ax.bar(temp_labels, average_revenues, color=colors)
        
#         # 막대 위에 데이터 값을 표시
#         for bar in bars:
#             yval = bar.get_height()
#             plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f} 억', ha='center', va='bottom', color='black', fontsize=10)

#         plt.title('애월읍 - 골프장 운영업 평균 매출 변화')
#         plt.xlabel('평균 기온 정렬')
#         # Streamlit에 그림 전달
#         st.pyplot()

#     # 데이터 로딩
#     data_list = []
#     for name in name_list:
#         filename = f'{name}_filtered_data.csv'
#         data = pd.read_csv(filename)
#         data_list.append(data)

#     # 웹 어플리케이션
#     st.title('[기온에 따른 업종별 매출변화]')
#     option = st.selectbox('원하는 지역을 선택해주세요', name_list)

#     # 선택한 지역의 데이터프레임 출력
#     st.write(f'## {option} 데이터')
#     selected_data = data_list[name_list.index(option)]
#     st.write(selected_data.head())

#     # 기온에 따른 업종별 매출 변화 그래프 출력
#     #st.write(f'### {option} - 골프장 운영업 평균 매출 변화')
    

#     # 데이터프레임으로 출력
#     st.write(f'### {option} - 업종별 평균 매출액 데이터')
#     for industry in industry_list:
#         st.write(f'{option} - {industry}')
#         plot_for_industry_t(selected_data, industry)    

# def tem_():
#     def plot_for_industry_t(data, industry):
#         industry_data = data[data['업종_분류'].str.contains(industry)]
    
#         # 평균 기온 구분별로 데이터 추출 및 평균 계산
#         temp_labels = ['시원함', '더위', '무더위', '추움']
#         average_revenues = []
#         for label in temp_labels:
#             temp_data = industry_data[industry_data['평균 기온 정렬'] == label]
#             average_revenue = temp_data['이용금액'].mean() / 1e8  # 단위를 억 원으로 변경
#             average_revenues.append(average_revenue)

#         # 선택한 지역의 업종별 매출 데이터 추출
#         selected_industry_data = selected_data[selected_data['업종_분류'].isin(industry_list)]
#         selected_industry_data = selected_industry_data.groupby(['업종_분류', '평균 기온 정렬'])['이용금액'].mean() / 1e8  # 억 원 단위로 변환
#         selected_industry_data = selected_industry_data.reset_index()

#         # '평균 기온 정렬' 열의 순서 변경
#         selected_industry_data['평균 기온 정렬'] = pd.Categorical(selected_industry_data['평균 기온 정렬'], 
#                                                               categories=['시원함', '더위', '무더위', '추움'], 
#                                                               ordered=True)
#         selected_industry_data = selected_industry_data.sort_values('평균 기온 정렬')
#         st.write(f'### {industry}에 대한 데이터프레임')
#         st.write(selected_industry_data)

#         # 그래프 생성
#         plt.ylabel('평균 매출액 (억 원)')
#         plt.figure(figsize=(10, 6))
#         ax = plt.gca()  # 현재 axes 가져오기
#         colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']  # 각 계절별 색상 설정
#         bars = ax.bar(temp_labels, average_revenues, color=colors)

#         # 막대 위에 데이터 값을 표시
#         for bar in bars:
#             yval = bar.get_height()
#             plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', color='black', fontsize=10)

#         plt.title(f'{option} - {industry} 평균 매출 변화')
#         plt.xlabel('평균 기온 정렬')
#         # Streamlit에 그림 전달
#         st.pyplot()

#     # 데이터 로딩
#     data_list = []
#     for name in name_list:
#         filename = f'{name}_filtered_data.csv'
#         data = pd.read_csv(filename)
#         data_list.append(data)

#     # 웹 어플리케이션
#     st.title('[기온에 따른 업종별 매출변화]')
#     option = st.selectbox('원하는 지역을 선택해주세요', name_list)

#     # 선택한 지역의 데이터프레임 출력
#     st.write(f'## {option} 데이터')
#     selected_data = data_list[name_list.index(option)]
#     st.write(selected_data.head())

#     # 선택한 지역의 업종별 평균 매출 데이터프레임과 그래프 출력
#     #st.write(f'## {option} - 업종별 평균 매출액 데이터')
#     for industry in industry_list:
#         st.subheader(f'{option} - {industry}')
#         plot_for_industry_t(selected_data, industry)

def tem_():
    def plot_for_industry_t(data, industry):
        industry_data = data[data['업종_분류'] == industry]  # 업종명 필터링

        # 평균 기온 구분별로 데이터 추출 및 평균 계산
        temp_labels = ['시원함', '더위', '무더위', '추움']
        temp_revenues = []
        for label in temp_labels:
            temp_data = industry_data[industry_data['평균 기온 정렬'] == label]
            average_revenue = temp_data['이용금액'].mean() / 1e8  # 억 원 단위로 변환
            temp_revenues.append(average_revenue)

        # 데이터프레임 생성
        temp_df = pd.DataFrame({
            '평균 기온 정렬': temp_labels,
            '평균 매출액 (억 원)': temp_revenues
        })

        st.write(f'### {industry}에 대한 데이터프레임')
        st.write(temp_df)

        # # 그래프 생성
        # plt.figure(figsize=(10, 6))
        # sns.barplot(x='평균 기온 정렬', y='평균 매출액 (억 원)', data=temp_df)
        # plt.title(f'{industry} 평균 매출 변화')
        # plt.xlabel('평균 기온 정렬')
        # plt.ylabel('평균 매출액 (억 원)')
        # 그래프 생성
        plt.figure(figsize=(10, 6))

        # 막대 그래프 그리기
        colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsalmon']  # 각 계절별 색상 설정
        sns.barplot(x='평균 기온 정렬', y='평균 매출액 (억 원)', data=temp_df, palette=colors)

        # 막대 위에 데이터 값을 표시
        ax = plt.gca()  # 현재 axes 가져오기
        for bar in ax.patches:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', color='black', fontsize=10)

        # 그래프 제목 및 축 레이블 설정
        plt.title(f'{industry} 평균 매출 변화')
        plt.xlabel('평균 기온 정렬')
        plt.ylabel('평균 매출액 (억 원)')

        st.pyplot()



    # 데이터 로딩
    data_list = []
    for name in name_list:
        filename = f'{name}_filtered_data.csv'
        data = pd.read_csv(filename)
        data_list.append(data)

    # 웹 어플리케이션
    st.title('[기온에 따른 업종별 매출 변화]')
    option = st.selectbox('원하는 지역을 선택해주세요', name_list)

    # 선택한 지역의 데이터프레임 출력
    st.write(f'## {option} 데이터')
    selected_data = data_list[name_list.index(option)]
    st.write(selected_data.head())

    # 기온에 따른 업종별 매출 변화 출력
    st.write(f'## {option} - 업종별 평균 매출액 데이터')
    for industry in industry_list:
        st.subheader(f'{option} - {industry}')
        plot_for_industry_t(selected_data, industry)