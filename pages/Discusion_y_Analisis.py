import streamlit as st
import pandas as pd

st.title("DISCUSIÓN Y ANÁLISIS")
st.header("Hallazgos Principales")

data = {
    "Terreno": ["Arena", "Concreto", "Césped", "Mulch", "Grava", "Tierra"],
    "Fuerzas netas delanteras (N)": ["15-21", "25-35", "18-26", "17-25", "18-25", "18-26"],
    "Fuerzas netas traseras (N)": ["70-75", "72-80", "78-88", "74-82", "78-86", "76-83"],
    "Estabilidad": ["Baja", "Muy alta", "Media", "Baja - Media", "Media - Alta", "Media - Alta"]
}

df = pd.DataFrame(data)

def color_estabilidad(val):
    val_lower = val.lower()
    
    if "muy alta" in val_lower:
        bg = "#23362A"
        fg = "#0FA145"
    elif "alta" in val_lower:
        bg = "#23362A"
        fg = "#0FA145"
    elif "media" in val_lower:
        bg = "#3A3423"
        fg = "#DE960F"
    elif "baja" in val_lower:
        bg = "#330000"
        fg = "#FF3037"
    else:
        bg = "white"
        fg = "black"
    return f"background-color: {bg}; color: {fg};"

st.dataframe(
    df.style.map(color_estabilidad, subset=["Estabilidad"]),
    width="stretch",
    )

st.markdown("""
    El robot concentra mayor fuerza en las **patas traseras** (≈70–85 N), especialmente la derecha, indicando que la **tracción principal** proviene de la parte posterior.  
    Las **patas delanteras** (≈15–35 N) actúan más en **dirección y estabilización**.
    """)

st.markdown("""
    - **Arena:** Superficie blanda y poco compacta; fuerzas delanteras irregulares y dispersas, traseras elevadas (≈70–75 N). El robot redistribuye carga hacia atrás para compensar la pérdida de apoyo.  
    - **Concreto:** Terreno rígido y estable; fuerzas limpias y constantes (delanteras ≈25–35 N, traseras ≈72–80 N). Locomoción más eficiente y equilibrada.              
    - **Césped:** Superficie semiblanda; fuerzas delanteras moderadas (≈18–26 N) y traseras más altas (≈78–88 N). Buen desempeño con ligera pérdida de eficiencia por compresibilidad.  
    - **Mulch (mantillo orgánico):** Terreno fibroso e inestable; fuerzas delanteras irregulares (≈17–25 N) y traseras fluctuantes (≈74–82 N). Se presentan deslizamientos intermitentes y mayor esfuerzo de corrección.  
    - **Grava:** Terreno granular con buena fricción; fuerzas delanteras cíclicas (≈18–25 N) y traseras regulares (≈78–86 N). Buena tracción con microajustes para estabilidad.  
    - **Tierra:** Superficie semiblanda y bien compactada; fuerzas equilibradas (delanteras ≈18–26 N, traseras ≈76–83 N) y patrón estable. Ofrece equilibrio entre adherencia y absorción.  
    """)
