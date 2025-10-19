import pandas as pd
import plotly.express as px
import streamlit as st

# Carga de datos (idealmente dentro de una función para cachearla con @st.cache_data)
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df = load_data("data/df_qcat_filtrado.csv")

nombres_patas = {
    "FL": "Delantera Izquierda (FL)",
    "FR": "Delantera Derecha (FR)",
    "BL": "Trasera Izquierda (BL)",
    "BR": "Trasera Derecha (BR)"
}

colores_patas = {
    nombres_patas["FL"]: "#1f77b4", # Azul
    nombres_patas["FR"]: "#ff7f0e", # Naranja
    nombres_patas["BL"]: "#2ca02c", # Verde
    nombres_patas["BR"]: "#d62728"  # Rojo
}

st.title("Comparación Dinámica de Fuerzas entre Patas")

col1, col2, col3, col4 = st.columns(4)

pata_x = col1.selectbox(
    "Elige la pata para el eje X",
    options= nombres_patas.keys(),
    format_func= lambda key: nombres_patas[key], 
    index= 0
)
pata_y = col3.selectbox(
    "Elige la pata para el eje Y",
    options= nombres_patas.keys(),
    format_func= lambda key: nombres_patas[key], 
    index= 1
)

eje_x = col2.selectbox("Elige el eje de la fuerza (X)", ("x", "y", "z"), index=0)
eje_y = col4.selectbox("Elige el eje de la fuerza (Y)", ("x", "y", "z"), index=1)

fig_scatter = px.scatter(
    df,
    x= f"{pata_x}_{eje_x}",
    y= f"{pata_y}_{eje_y}",
    opacity= 0.6,
    labels= { 
        f"{pata_x}_{eje_x}": f"Fuerza en eje '{eje_x.upper()}' de la pata {nombres_patas[pata_x]}",
        f"{pata_y}_{eje_y}": f"Fuerza en eje '{eje_y.upper()}' de la pata {nombres_patas[pata_y]}"
    },
    title= f"Comparación de Fuerza '{eje_x.upper()}' ({nombres_patas[pata_x]}) vs. '{eje_y.upper()}' ({nombres_patas[pata_y]})"
)

fig_scatter.update_traces(marker =dict(size= 5))
fig_scatter.update_layout(template= "plotly_white")
st.plotly_chart(fig_scatter, use_container_width= True)

st.divider()
st.header("Análisis de la Magnitud de Fuerza Promedio por Pata")

for pata_code in nombres_patas.keys():
    df[f"{pata_code}_total"] = (df[f"{pata_code}_x"]**2 + df[f"{pata_code}_y"]**2 + df[f"{pata_code}_z"]**2)**0.5

columnas_fuerza_total = [f"{pata_code}_total" for pata_code in nombres_patas.keys()]
avg_forces = df[columnas_fuerza_total].mean().reset_index()
avg_forces.columns = ["Código Pata", "Fuerza Promedio (N)"]

avg_forces["Pata"] = avg_forces["Código Pata"].str.replace("_total", "")
avg_forces["Pata"] = avg_forces["Pata"].map(nombres_patas)


fig_bar = px.bar(
    avg_forces,
    x= "Pata",
    y= "Fuerza Promedio (N)",
    color= "Pata",
    color_discrete_map= colores_patas, 
    title= "Magnitud de Fuerza Promedio por Pata del Robot",
    labels= {"Pata": "Pata del Robot"} 
)

fig_bar.update_traces(textposition= 'outside')
fig_bar.update_layout(
    template= "plotly_dark",
    yaxis_title= "Fuerza Promedio (N)",
    xaxis_title= "Pata del Robot",
    showlegend= False
)

st.plotly_chart(fig_bar)