import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# --- Función para convertir imagen PIL o ruta a base64 ---
def image_to_base64(image_path):
    if isinstance(image_path, Image.Image):
        img = image_path
    else:
        img = Image.open(image_path)
    buffer = BytesIO()
    img.save(buffer, format="WEBP")
    return base64.b64encode(buffer.getvalue()).decode()

image_path = "public/DyRET.webp"
img_base64 = image_to_base64(image_path)

st.title("INTRODUCCIÓN Y PLANTEAMIENTO DEL PROBLEMA")

st.markdown(f"""
    <div style='text-align: center; margin-top: 20px;'>
        <img src='data:image/webp;base64,{img_base64}' 
             style='width:400px;' alt='DyRET Robot'/>
        <p style='font-size:14px; margin-top:5px;'>
            <a href='https://theconversation.com/shape-shifting-robots-in-the-wild-the-dyret-robot-can-rearrange-its-body-to-walk-in-new-environments-157130'
               target='_blank' style='color:#1c77f8; text-decoration:none;'>
               Fuente: Ilustración del robot DyRET realizada por cuenta propia.
            </a>
        </p>
    </div>
""", unsafe_allow_html=True)
st.subheader("Contexto")
st.markdown("""
Los **robots cuadrúpedos bioinspirados** representan un campo de rápido desarrollo en la robótica, destacando por su capacidad para adaptarse a terrenos complejos y realizar tareas en ambientes desafiantes.
""")

st.divider()

st.subheader("Sensores Integrados")
st.markdown("""
Para lograr una interacción precisa con su entorno, el robot está equipado con dos tipos de sensores avanzados:

* **Sensores de Fuerza (RAW):** En el extremo de cada una de las cuatro patas se encuentra un sensor de fuerza de tres ejes (*Optoforce OMD-20-SH-80N*). Este dispositivo es crucial para registrar las fuerzas de contacto con el suelo en los ejes X, Y y Z.

* **Unidad de Medición Inercial (IMU):** Se incorpora una IMU (*Xsens MTI-30*) que integra:
    * Un **giroscopio** de tres ejes para medir velocidades de rotación.
    * Un **acelerómetro** de tres ejes para registrar aceleraciones lineales.
    * Un **magnetómetro** de tres ejes que proporciona la orientación absoluta del robot con respecto al campo magnético terrestre.
""")