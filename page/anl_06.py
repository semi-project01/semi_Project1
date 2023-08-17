from utils import anl_mo_06_01 as am6
import streamlit as st

def app():    
    st.title('[기온에 따른 업종별 매출 변화]')
    am6.tem_()