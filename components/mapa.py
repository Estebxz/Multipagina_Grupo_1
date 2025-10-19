import streamlit as st
import folium

from streamlit_folium import st_folium

def mapa_interactivo():
    latitude = -27.4698
    longitude = 153.0251
    
    m = folium.Map(location=[latitude, longitude], zoom_start= 4, min_zoom= 4, max_zoom= 16)

    folium.Marker(
        [latitude, longitude], 
        tooltip="Lugar de recolección de datos"
    ).add_to(m)

    def callback():
        st.toast(f"Nivel de zoom actual: {st.session_state['my_map']['zoom']}")
    
    st.subheader("Ubicacion de recolección de datos - Brisbane, 🇦🇺 Australia")
    st_folium(m, width=725, height=500, key="my_map" , on_change=callback)
    