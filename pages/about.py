from components.star_github import footer_component
import streamlit as st

st.title("ℹ️ Acerca de")
st.write(
    """
    Esta aplicación ha sido desarrollada con **Streamlit** como parte de un proyecto de formación
    en desarrollo Full Stack e inteligencia artificial.

    Su objetivo es ofrecer una experiencia educativa y práctica para analizar datos, construir
    interfaces web dinámicas y aplicar técnicas modernas de desarrollo.
    """
)

st.divider()

st.subheader("👨‍💻 Autor")
st.write(
    """
    **Desarrollado por:** Joan Esteban Méndez  
    **Rol:** Desarrollador Full Stack & Analista de Datos  
    **GitHub:** [joanestebandev](https://github.com/joanestebandev)
    """
)

st.divider()

st.subheader("🛠️ Tecnologías utilizadas")
st.markdown(
    """
    - **Python** 🐍  
    - **Streamlit** para la interfaz interactiva  
    - **Pandas**, **Matplotlib** y **Scikit-learn** para el análisis de datos  
    - **Docker** para contenerización  
    - **GitHub Actions** para automatización del despliegue
    """
)

footer_component()