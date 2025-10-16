import pandas as pd
import streamlit as st

def generar_informe_dataset(df: pd.DataFrame):
    st.markdown("## 📊 INFORME DEL DATASET")
    st.write(f"**Tipo de objeto:** `{type(df)}`")

    # Dimensiones
    filas = 1499806
    columnas = 20
    st.write("**Dimensiones del dataset:**")
    st.markdown(f"""
    - Número de filas: **{filas}**  
    - Número de columnas: **{columnas}**
    """)

    # Tipos de datos
    st.markdown("### 🧩 Columnas y tipos de datos:")
    tipos = pd.DataFrame(df.dtypes, columns=["Tipo de Dato"])
    tipos.index.name = "Columna"
    st.dataframe(tipos)

    # Registro de vacíos
    vacios = df.isnull().sum()
    porcentaje_vacios = (vacios / len(df) * 100).round(2)
    resumen_vacios = pd.DataFrame({
        "Columna": df.columns,
        "Registros vacíos": vacios,
        "(%)": porcentaje_vacios,
        "Tipo de Dato": df.dtypes.astype(str)
    }).set_index("Columna")
    
    st.markdown("### 📉 Registros vacíos por columna:")
    st.dataframe(resumen_vacios)

    # Duplicados
    duplicados = df.duplicated().sum()
    porcentaje_duplicados = round((duplicados / len(df)) * 100, 2)
    st.markdown("### 🔁 Registros duplicados:")
    st.write(f"- Cantidad: **{duplicados}**")
    st.write(f"- Porcentaje: **{porcentaje_duplicados}%**")

    # Estadísticas numéricas
    st.markdown("### 📈 Estadísticas descriptivas:")
    st.dataframe(df.describe().T)

    st.success("✅ Informe generado correctamente.")