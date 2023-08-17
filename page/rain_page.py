from utils import rain_mo as ra
import streamlit as st

def app():    
    st.title('[일강수량에 따른 업종별 매출변화]')
    ra.rain()

