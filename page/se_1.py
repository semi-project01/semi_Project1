import streamlit as st
from utils import se_1_mo as sm1


def app():
    st.write('데이터프레임 및 맵플롯 구간입니다.')
    df = sm1.get_movie()
    st.dataframe(df)