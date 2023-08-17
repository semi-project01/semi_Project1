from utils import result_mo as res
import streamlit as st

def app():    
    st.title('[계절에 따른 업종별 매출 변화]')
    res.result()