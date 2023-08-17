from utils import wind_mo as win
import streamlit as st

def app():
    st.title('[최대 풍속에 따른 업종별 매출변화]')
    win.wind()

