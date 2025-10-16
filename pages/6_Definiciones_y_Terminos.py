import streamlit as st
from components.star_github import footer_component

st.markdown("""
## 📘 Definiciones y Términos

---

### ⚙️ **Sensor RAW**
Datos sin procesar obtenidos directamente de los sensores del robot.  
En este caso, se trata de las mediciones de **fuerza y posición** antes de cualquier filtrado o procesamiento.

---

### 🧭 **IMU (Unidad de Medición Inercial)**
Dispositivo **Xsens MTI-30** que integra un **giroscopio**, un **acelerómetro** y un **magnetómetro**,  
permitiendo medir **velocidades angulares**, **aceleraciones lineales** y **orientación** respecto al campo magnético terrestre.

---

### 🧩 **Fx, Fy, Fz**
Componentes de la **fuerza medida por cada pata** en los distintos ejes:
- **X:** Dirección horizontal  
- **Y:** Dirección lateral  
- **Z:** Dirección vertical  

---

### 🚶‍♂️ **Velocidad de marcha**
Frecuencia o ritmo al que el robot avanza.  
Puede estar asociada a una **frecuencia en Hz**, indicando la cantidad de pasos por segundo.
""")

footer_component()