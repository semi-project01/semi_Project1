import streamlit as st
from utils import anl_mo_02_00 as am0200
from utils import anl_mo_02_01 as am0201
from utils import anl_mo_02_02 as am0202
from utils import anl_mo_02_03 as am0203

def app():
	st.write('''
		## 2018-2019 강수량&풍속&기온의 흐름
		'''
		)

	am0200.desc()
    
	st.write('''
		## 2018-2019 월 강수량
		'''
		)

	am0201.desc02()
    
	st.write('''
		## 2018-2019 최대 풍속
		'''
		)

	am0202.desc03()
    
	st.write('''
		## 2018-2019 평균 기온
		'''
		)

	am0203.desc04()
