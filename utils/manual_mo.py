import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    st.markdown('----')
    #st.header
    st.code('''
            • 텍스트를 헤더로 출력(타이틀보다 작음)
            - st.header('Header) :         
            ''') 
    st.write('''예시)''')
    st.title("Header")
    st.markdown('----')
    #st.write   
    st.code('''
            • 기본적인 텍스트르 작성해주는 method
            - st.write('Hellow world')
            ''') 
    st.write('''예시)''')
    st.write('Hello world')
    st.markdown('----')
    # st.sidebar
    st.code('''
            • 웹페이지 왼쪽에 사이드바를 추가   
            - st.sidebar.selectbox('메뉴 선택하세요', ['선택1', '선택2','선택3'])
            - ( )안에 메뉴 상단 문구 작성, 희망 selectbox를 리스트 또는 튜플로 추가해주시면 됩니다.
            ''')
       
    st.write('''예시)''')
    st.image('image/side.png')
    st.markdown('----')
    #st.button
    st.code('''
            • 사용자가 클릭할 수 있는 버튼을 생성
            - st.button('실행버튼')
            ''') 
    st.write('''예시)''')
    st.button('실행버튼')
    
    st.markdown('----')
    #st.pyplot
    st.code('''
            • matplotlib을 통해 생성된 그래프를 출력
            - st.pyplot()
            ''') 
    st.write('''예시)''')
    st.code('''
            df = pd.DataFrame(np.arange(15))
            fig, ax = plt.subplots(figsize=(5, 5))
            
            ax.plot(df)
            st.pyplot()
            ''')
    df = pd.DataFrame(np.arange(15))
    fig, ax = plt.subplots(figsize=(5, 5))  # plt.subplots() 수정
    ax.plot(df)
    st.pyplot(fig)

    st.markdown('----')
    #dataframe
    st.code('''
            • 데이터프레임을 불러오는 method
            - st.dataframe()
            ''') 
    st.write('''예시)''')
    st.code('''
            data = {
                "이름": ["Alice", "Bob", "Charlie"],
                "나이": [25, 30, 28],
                "직업": ["개발자", "디자이너", "마케터"]
                }
            
            df = pd.DataFrame(data)

            st.dataframe(df)


            ''') 
    
    data = {
        "이름": ["Alice", "Bob", "Charlie"],
        "나이": [25, 30, 28],
        "직업": ["개발자", "디자이너", "마케터"]
        }
            
    df = pd.DataFrame(data)
      
    st.dataframe(df)
 
    

