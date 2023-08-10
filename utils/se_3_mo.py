from streamlit_folium import folium_static
import streamlit as st
import folium


def foliummap(data):
    st.header('가본 곳')
    m = folium.Map(location=[37.5602, 126.982], zoom_start=11)
    #tooltip = "Liberty Bell"
    #folium.Marker([37.5602, 126.982], popup="Liberty Bell", tooltip=tooltip).add_to(m)
    for i_name in data:
        tooltip = i_name
        lat_long = data[i_name]
        folium.Marker(data[i_name], popup=i_name, tooltip=tooltip).add_to(m)
    folium_static(m)


data = {
'Eoleumgol' : [35.570678, 128.986135],
'Bangujeong' : [37.867614, 126.752505], 'Abgujeong':[37.531713, 127.029154],
'금강소나무숩': [36.985459, 129.205468],
'Heonanseolheonmyo': [37.425569, 127.296012],
'Baegdamsa': [38.164890, 128.374023],
'Moagsan mileugbul' : [35.723051, 127.053816],
'Hailli' : [37.680120, 126.398192],
'Ieodo': [32.116883, 125.166683],
'Bughansan' : [37.659318, 126.9775415],
'Ondalsanseong' : [37.057707, 128.484972],
'Cheonglyeongpo' : [37.176118, 128.445583],
'Hansanseom' : [34.816761, 128.423040],
'해인사' : [35.801479, 128.098052],
'Sancheonjae' : [35.275175, 127.849891],
'Seomjingang' : [34.963452, 127.760620],
'Baegheungam' : [35.994240, 128.778653],
'Guksaseonangdang': [37.696354, 128.753741],
'Mudeungsan' : [35.134134, 126.988756],
'부산성' : [36.268112, 126.914802]}