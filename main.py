import streamlit as st

st.set_page_config(
    page_title="Dashboard TTCH",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)

grupo_1 = [
    st.Page("pages/course_overview.py", title="Resumen del Curso", icon="📚"),
    st.Page("pages/1_Introduccion.py", title="Modulo 1: Introducción", icon="👋"),
    st.Page("pages/2_Resumen_Ejecutivo.py", title="Modulo 2: Resumen Ejecutivo", icon="📝"),
    st.Page("pages/3_Objetivos.py", title="Modulo 3: Objetivo general y específicos", icon="🎯"),
    st.Page("pages/4_Alcance_y_Problema.py", title="Modulo 4: Alcance y Identificación del problema", icon="🚀"),
    st.Page("pages/5_Contexto_y_Antecedentes.py", title="Modulo 5: Contexto y Antecedentes", icon="🌍"), 
    st.Page("pages/6_Definiciones_y_Terminos.py", title="Modulo 6: Definiciones y Términos", icon="📖"), 
    st.Page("pages/7_Metodologia.py", title="Modulo 7: Metodología", icon="🛠️"), 
    st.Page("pages/8_Acceso_y_Recoleccion.py", title="Modulo 8: Acceso y Recolección de Datos", icon="📊"), 
    st.Page("pages/9_Formato_y_Estructura.py", title="Modulo 9: Formato y Estructura de Datos", icon="🗂️"), 
    st.Page("pages/10_Procesamiento_y_Resultados.py", title="Modulo 10: Procesamiento y Resultados de Datos", icon="⚙️"), 
    st.Page("pages/11_Discusion_y_Conclusiones.py", title="Modulo 11: Discusión y Conclusiónes", icon="💡"), 
    st.Page("pages/12_Referencias_Bibliograficas.py", title="Modulo 12: Referencias Bibliográficas", icon="📚"),
]

datasets = [
    st.Page("pages/graphics.py", title="Graficos", icon="📈"),
]

extra = [
    st.Page("pages/contact.py", title="Contacto", icon="📞"),
    st.Page("pages/about.py", title="Acerca de", icon="🌐"),
]

pages = {
    "💻 Grupo_1": grupo_1,
    "📂 Recursos": datasets,
    "⚙️ Otros": extra
}

pg = st.navigation(pages)
pg.run()