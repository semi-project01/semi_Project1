from utils import seaseon_mo as sm
import streamlit as st

def app():    
    st.title('[계절에 따른 업종별 매출 변화]')
    sm.get()

