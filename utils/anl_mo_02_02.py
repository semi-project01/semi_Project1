#2018-2019최대풍속
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def desc03():
    df = pd.read_csv('cleaned_data.csv')

    selected_columns = ['일자', '읍면동명', '평균 기온', '일강수량', '최대 풍속', '업종명', '이용금액']
    selected_df = df[selected_columns]

    selected_df['일자'] = pd.to_datetime(selected_df['일자'])
    selected_df['Year'] = selected_df['일자'].dt.year
    
    plt.style.use('ggplot')

    # 평균 기온 그래프
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))

    # 평균 기온 그래프 (2018년과 2019년 분리)
    for year, color in zip([2018, 2019], ['darkorange', 'forestgreen']):
        year_data = selected_df[selected_df['Year'] == year]
        monthly_mean_df = year_data.groupby(year_data['일자'].dt.to_period('M')).mean()
        ax.plot(monthly_mean_df.index.strftime('%b'), monthly_mean_df['최대 풍속'], marker='o', color=color, label=f'{year}') 
        ax.legend()
        ax.set_title('Monthly MAX Wind Speed (2018 and 2019)')
        ax.set_xticks(monthly_mean_df.index.strftime('%b'))
        ax.set_xticklabels(monthly_mean_df.index.strftime('%b'))

    plt.tight_layout()
    st.pyplot(plt)
