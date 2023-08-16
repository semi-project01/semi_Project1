import streamlit as st
from utils import anl_mo_05_01 as am0501
from utils import anl_mo_05_01 as am0502

def app():
	st.write('''
		## 2018-01~2020-04 평균기온서의 업종별매출
		'''
		)

	am0501.desc()
    
	st.write('''
		## 2018, 2019년도 평균기온에서의 업종별 매출 비교
		'''
		)

	am0502.desc02()
