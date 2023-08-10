import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#from utils import se_1_mo as sm1


def get_plot():
    df = pd.DataFrame(np.arange(15))
    fig, ax = plt.subplots(figsize=(8, 8))  # plt.subplots() 수정
    ax.plot(df)
    st.pyplot(fig)