import streamlit as st
from utils import se_3_mo as sm3

def app():
    st.write('3번을 선택했습니다.')
    user_input = st.text_input('글을 입력한 후 버튼을 눌러주세요')
    button = st.button('실행버튼')
    if button:
        st.write('버튼을 눌렀기 떄문에 다음 문장이 출력됩니다')
        st.write(user_input)
    sm3.foliummap(sm3.data)