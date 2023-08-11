# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:38:30 2023

@author: goldg
"""

import streamlit as st

def desc():
    st.write('''
            ### 1. Powershell Prompt를 실행 합니다.
            ### 2. conda env list 를 입력합니다.
                 이것은 현재 아나콘에 있는 가상환경 목록을 보여줍니다.
            ''')

    st.image('image\image01.png', use_column_width = True)

    st.write('''
            ### 3. conda create -n semiproject python=3.9 ipython numpy pandas matplotlib folium
                            
                semiproject이란 가상환경 이름으로 파이썬 버전을 정해주고
            
                설치하고자 하는 라이브러리들를 적어줍니다.
            
                이 때 streamlit은 아나콘다의 repository에 없어서 에러가 발생하므로 나중에 설치해 줍니다.
            ''')
    st.image('image\image02.png') #y누르는 부분
    st.write('''
            ### 4. 설치 완료
            
            conda activate semiproject : semiproject 가상환경을 실행합니다.
                
    codna deactivate : 가상환경을 나옵니다.
            ''')
    st.image('image\image03.png')
    st.write('''
             ### 5. 제대로 설치가 되어있는 확인하는 단계
             
                 pyhthon --version : 파이선의 버전을 확인하는 명령어 입니다.
             
             ''')
    st.image('image\image04.png')
    