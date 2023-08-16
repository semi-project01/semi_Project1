import streamlit as st
from utils import anl_mo_03_01 as am0301
from utils import anl_mo_03_02 as am0302

def app():
	st.write('''
		## 2018-01~2020-04 강수량에서의 업종별 매출 비교
		'''
		)

	am0301.desc()
    
	st.write('''
		## 2018, 2019년도 강수량에서의 업종별 매출 비교
		'''
		)

	am0302.desc02()
