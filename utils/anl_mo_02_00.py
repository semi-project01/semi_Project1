#3년치 온도 강수량 풍속 비교 그래프
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def desc():
    df = pd.read_csv('cleaned_data.csv')

    selected_columns = ['일자', '읍면동명', '평균 기온', '일강수량', '최대 풍속', '업종명', '이용금액']
    selected_df = df[selected_columns]

    selected_df['일자'] = pd.to_datetime(selected_df['일자'])
    monthly_sum_df = selected_df.groupby(selected_df['일자'].dt.to_period('M')).sum()
    monthly_mean_df = selected_df.groupby(selected_df['일자'].dt.to_period('M')).mean()
    


    plt. style.use('ggplot')
    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    #평균 기온 그래프
    ax1.plot([month.strftime('%Y-%m') for month in monthly_sum_df.index], monthly_mean_df['평균 기온'], marker='o', markerfacecolor='g', color='olive', markersize=10, linewidth=2, label='Average Temperatures')
    ax1.legend(loc='best')
    ax1.set_title('Monthly Average Temperatures', size=20, y=1.02)
    ax1.set_xticklabels([month.strftime('%Y-%m') for month in monthly_sum_df.index], rotation='vertical')

    #일강수량 그래프
    ax2.plot([month.strftime('%Y-%m') for month in monthly_sum_df.index], monthly_mean_df['일강수량'], marker='o', markerfacecolor='b', color='skyblue', markersize=10, linewidth=2, label='Day Precipitation')
    ax2.legend(loc='best')
    ax2.set_title('Monthly Day Precipitation', size=20, y=1.02)
    ax2.set_xticklabels([month.strftime('%Y-%m') for month in monthly_sum_df.index], rotation='vertical')
    
    #최대풍속 그래프
    ax3.plot([month.strftime('%Y-%m') for month in monthly_sum_df.index], monthly_mean_df['최대 풍속'], marker='o', markerfacecolor='r', color='crimson', markersize=10, linewidth=2, label='MAX Wind Speed')
    ax3.legend(loc='best')
    ax3.set_title('Monthly MAX Wind Speed', size=20, y=1.02)
    ax3.set_xticklabels([month.strftime('%Y-%m') for month in monthly_sum_df.index], rotation='vertical')
    
    plt.tight_layout()
    st.pyplot(plt)