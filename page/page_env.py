import streamlit as st
from utils import utils_env as utenv

def app():
	st.title('가상환경 구축 메뉴얼'
		)

	utenv.desc()
    