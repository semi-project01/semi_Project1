import streamlit as st
from utils import anl_mo_04_01 as am0401
from utils import anl_mo_04_02 as am0402

def app():
	st.write('''
		## 2018-01~2020-04 최대풍속에서의 업종별매출
		'''
		)

	am0401.desc()
    
	st.write('''
		## 2018, 2019년도 최대풍속에서의 업종별 매출 비교
		'''
		)

	am0402.desc02()

