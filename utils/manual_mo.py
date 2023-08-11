import streamlit as st
import pandas as pd


def manual_():
    st.write('''
    #### 1. streamlit 이란 
    - 머신러닝이나 데이터 사이언스에 특화된 웹 어플리케이션을 쉽게 만들고 공유하도록 해주는 파이썬 오픈소스 라이브러리이다.
    
    - 인터랙티브한 기능을 제공하며, 다양한 method를 통해 text, 이미지, dataframe 등을 표현할 수 있다.
    
    #### 2.사용순서
    - pip install stramlit 이라는 코드를 통해 설치를한다.
    
    - import streamlit as st 를 입력하여 해당 라이브러리를 불러온다.
    
    - 필요에 따라 다른 라이브러리를 불러온 후 다양한 method를 사용하여 활용한다.
    ''')
    st.write('''
    #### 3. 다양한 method
    ''')
    #st.title
    st.code('''
            • 텍스트를 타이틀로 출력.
            - st.title("Title")
            ''') 
    st.write('''예시)''')
    st.title("Title")
    
    #st.header
    st.code('''
            • 텍스트를 헤더로 출력(타이틀보다 작음)
            - st.header('Header) :         
            ''') 
    st.write('''예시)''')
    st.title("Header")
    
    #st.write   
    st.code('''
            • 기본적인 텍스트르 작성해주는 method
            - st.write('Hellow world')
            ''') 
    st.write('''예시)''')
    st.write('Hello world')
    
    # st.sidebar   
    st.code('''
            • 웹페이지 왼쪽에 사이드바를 추가   
            - st.sidebar.selectbox('메뉴 선택하세요', ['선택1', '선택2','선택3'])
            - ( )안에 메뉴 상단 문구 작성, 희망 selectbox를 리스트 또는 튜플로 추가해주시면 됩니다.
            ''')
     
    st.write('''예시)''')
    st.write('Hello world')
    
    st.write('''
    - st.sidebar.selectbox() 화면측면에 체크박스를 생성
    ##### 예시)''')
    st.image('image/side.png')
    st.write('''
    - st.button() 사용자가 클릭할 수 있는 버튼을 생성
    ##### 예시)''')
    st.image('image/button.png')
    st.write('''
    - st.pyplot() matplotlib을 통해 생성된 그래프를 출력
    
    - st.dataframe() 데이터프레임을 불러오는 method
    ''')


