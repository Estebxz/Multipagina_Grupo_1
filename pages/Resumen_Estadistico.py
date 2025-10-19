import streamlit as st
from components.resumen_estadistico import generar_informe_dataset
from components.star_github import footer_component

generar_informe_dataset("data/df_qcat_filtrado.csv")
footer_component()