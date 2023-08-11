# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:38:30 2023

@author: goldg
"""

import streamlit as st

def desc():    
    st.write('''
            ### 1. 먼저 Powershell Prompt를 실행 합니다.
            ### 2. 현재 가지고 있는 가상환경을 확인합니다.
                
                -명령어 : conda env list 를 입력합니다.
                -현재 아나콘에 있는 가상환경 목록을 보여줍니다.
            ''')
    st.write('입력 후 아래와 같이 확인됩니다.')   
    st.image('image\image01.png', use_column_width = True)
    st.write("기본 'base'와 가상공간 'prjsmi'이 확인됩니다.")    
    st.write('''
            ### 3.새 가상환경 만들기(파이썬 버전 및 라이브러리)
             ''')
    st.code('''
            '가상공간' 형성 명령어 예시
            conda create -n semiproject python=3.9 ipython numpy pandas matplotlib folium

            #conda create -n semiproject 
            'semiproject'라는 이름의 가상공간을 만듭니다.

            #python=3.9 ipython
            '3.9버전 파이썬'으로 설치를 진행합니다.

            #numpy pandas matplotlib folium
            필요한 라이브러리 4가지를 함께 설치를 진행합니다.
            (numpy, pandas, matplotlib, folium)
            ''')
    st.write('''semiproject이란 가상환경 이름으로 파이썬 버전을 정해주고, 설치하고자 하는 라이브러리들를 마지막 뒤에 적어줍니다.
             ''')
    
    
    st.image('image\image02.png') #y누르는 부분
    st.markdown('<span style="padding-left: 220px; white-space: pre; font-size: 15px; font-weight: bold; color: red;">procceed 질문이 나오면 \':red[y]\'를 눌러주세요</span>', unsafe_allow_html=True)
    #st.markdown("procceed 질문이 나오면 '[y]'를 눌러주세요")
    st.image('image\image03.png',use_column_width = True)
    
    st.markdown('''
                설치를 끝마치면 'done'이라는 메세지와 함께 가상환경 생성이 되었습니다.
                ''')
    st.write('''
            ### 4. 가상환경 활성화 및 비활성화 
            ''')
    st.code('''
            - 'semiproject 가상환경'을 실행합니다.
            conda activate semiproject
            ''')
                
    st.code('''
            - '가상환경'을 나옵니다.
            codna deactivate 
                        ''')
    
    # 여기 이미지 활성화 비활성화 이미지 변경하는게 좋을 것 같음 

    st.write('''
             ### 5. 설치 확인 및 가상환경 실행
             ''')
    st.code('''
            - '파이선의 버전'을 확인하는 명령어 입니다.
            pyhthon --version 
            ''')
    st.image('image\image04.png')
    st.markdown('''기본 base는 파이썬 버전 3.10버전이지만 새로 가상환경에서는 3.9버전으로 설치가 되었음을 확인 가능합니다.
''')

    st.markdown('이후 streamlit라이브러리를 이용하여 웹 페이지를 확인이 가능합니다.')    
    st.markdown('----')
    st.markdown('<span style="font-weight: bold; color: gray"> * 이 때 streamlit은 아나콘다의 repository에 없어서 에러가 발생하는 경우 별도 설치해 줍니다.</span>', unsafe_allow_html=True)
    #st.write('''이 때 streamlit은 아나콘다의 repository에 없어서 에러가 발생하는 경우 별도 설치해 줍니다.''')
    st.markdown('<span style="padding-left: 220px; white-space:pre; font-size: 20px; font-weight: bold; color: red">pip install streamlit</span>', unsafe_allow_html=True)
    st.markdown('----')    