import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils import se_2_mo as sm2
#from utils import se_1_mo as sm1


def app2():
    st.write('2번을 선택했습니다.')
    sm2.get_plot()