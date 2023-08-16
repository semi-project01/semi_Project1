import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

from utils import anl_mo_01 as am1
from utils import anl_mo_01_2 as am1_2

def app():
    st.title('분석 01 - CSV파일 데이터 확인하기' )

    am1.total_check()
    am1.sort_data()
    am1_2.total_check1()
    am1_2.total_check2()
    am1_2.total_check3()