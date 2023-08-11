# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 13:34:06 2023

@author: goldg
"""

import streamlit as st
from utils import utils_env as utenv

def app():
	st.title('가상환경 구축 메뉴얼'
		)

	utenv.desc()
    