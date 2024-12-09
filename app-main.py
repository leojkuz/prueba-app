import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import reveal_slides as rs


# Configuración inicial de la página
st.set_page_config(page_title="Análisis Global de la Anemia", layout="wide")

# Colocar el logo de la universidad en la parte superior
st.sidebar.image("imagenes/escudo-unalm.png", use_column_width=True)
with st.sidebar:
    # Menú principal (vertical) en el sidebar
    menu = option_menu(
        menu_title="Menú Principal",  # Título del menú
        options=["Introducción", "Fuentes de datos", "Visualización de datos", "Conclusiones", "Equipo"],  # Opciones
        icons=["info-circle", "database", "bar-chart", "clipboard", "people"],  # Íconos si quieres
        menu_icon="cast",  # Ícono principal del menú
        default_index=0,  # Primera opción seleccionada por defecto
        orientation="vertical",
    )



# Contenido dinámico según opción seleccionada
if menu == "Introducción":
    st.title("Introducción")
    st.markdown("""
    ## ¿Qué es la anemia?
    La **anemia** es una condición médica caracterizada por un nivel bajo de hemoglobina en la sangre, lo que resulta en una capacidad reducida para transportar oxígeno al cuerpo. Esto puede ocasionar fatiga, debilidad y otros problemas de salud.

    ### Principales causas y tipos
    - **Deficiencia de hierro (anemia ferropénica):** La causa más común a nivel mundial.
    - **Anemia megaloblástica:** Por deficiencias de vitamina B12 o ácido fólico.
    - **Anemia hemolítica:** Resultado de la destrucción prematura de los glóbulos rojos.

    ### Importancia del análisis global
    Evaluar la prevalencia global y los factores asociados a la anemia es esencial para informar políticas públicas que mejoren la calidad de vida de las personas.

    *(¡Inserta aquí más texto académico o markdown estilizado si lo necesitas!)*
    
    ### Un vistazo a la situación de la anemia en el mundo
    """)
    st.write("")
    st.write("")
    # Configuración del contenido en Markdown para los slides
    content_markdown = """
    ## Presentation Features
    - Create slides from markdown or markup <!-- .element: class="fragment" data-fragment-index="0" -->
    - Touch, mouse, and keyboard navigation <!-- .element: class="fragment" data-fragment-index="1" -->
    - Fullscreen and overview modes <!-- .element: class="fragment" data-fragment-index="2" -->
    - Search and Zoom (plugins) <!-- .element: class="fragment" data-fragment-index="3" -->
    - Display LaTeX and syntax highlighted code (plugins) <!-- .element: class="fragment" data-fragment-index="4" -->
    ---
    ## Slide Content Creation
    A paragraph with some text and a markdown [link](https://hakim.se). 
    Markdown links get displayed within the parent iframe.
    --
    Another paragraph containing the same <a target="_blank" href="https://hakim.se">link</a>.
    However, this link will open in a new tab instead. 
    This is done using an HTML `<a>` tag with `target="_blank"`.
    ---
    ## Backgrounds
    Reveal supports four different types of backgrounds: color, image, video and iframe.
    --
    <!-- .slide: data-background-color="#283747" -->
    Change the background to a solid color using the `data-background-color` attribute.
    --
    <!-- .slide: data-background-video="https://bouzidanas.github.io/videos/pexels-cottonbro-9665235.mp4" data-background-video-loop data-background-video-muted -->
    Add a video as the background using the `data-background-video` attribute. Add `data-background-video-loop` to loop the video in the background and add `data-background-video-muted` to mute it.
    ---
    """

    # Creación del layout con columnas
    col1, col2, col3 = st.columns([1, 2, 1])  # Relación: 1:2:1 para centrar

    with col2:  # Contenido en la columna central
        response_dict = rs.slides(content_markdown, height = 500)

elif menu == "Fuentes de datos":
    st.title("Fuentes de Datos")

    # Submenú Horizontal
    sub_menu = option_menu(
        menu_title="",  # Sin título en el menú horizontal
        options=["Fuente 1", "Fuente 2", "Fuente 3"],
        icons=["link-45deg", "link-45deg", "link-45deg"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if sub_menu == "Fuente 1":
        st.subheader("Descripción Fuente 1")
        st.write("Datos recopilados de XXX institución, incluyendo estadísticas a nivel mundial del año XXXX.")

    elif sub_menu == "Fuente 2":
        st.subheader("Descripción Fuente 2")
        st.write("Información extraída del reporte anual de salud pública global por OMS.")

    elif sub_menu == "Fuente 3":
        st.subheader("Descripción Fuente 3")
        st.write("Estudios académicos con datos centrados en poblaciones específicas para análisis detallado.")

elif menu == "Visualización de datos":
    st.title("Visualización de Datos")

    # Submenú Horizontal para visualizaciones
    viz_menu = option_menu(
        menu_title="",
        options=["Situación Global", "Análisis por País", "Proyecciones", "Factores Relacionados"],
        icons=["globe", "bar-chart-steps", "graph-up-arrow", "table"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    if viz_menu == "Situación Global":
        st.subheader("Situación Global de la Anemia")

        # Mini dashboard con gráficos simples inventados
        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            ax.pie([70, 30], labels=["Población sin anemia", "Población con anemia"], autopct="%1.1f%%")
            ax.set_ylabel("")
            st.pyplot(fig)

        with col2:
            st.metric(label="Prevalencia General (%)", value="30%")
            st.metric(label="Región más afectada", value="África Subsahariana")

    elif viz_menu == "Análisis por País":
        st.subheader("Análisis por País")

        # Gráfico de barras inventado
        countries = ["País 1", "País 2", "País 3", "País 4"]
        values = [45, 30, 22, 10]

        fig, ax = plt.subplots()
        ax.bar(countries, values, color="skyblue")
        ax.set_title("Prevalencia de Anemia por País (%)")
        st.pyplot(fig)

    elif viz_menu == "Proyecciones":
        st.subheader("Proyecciones Futuras")

        # Gráfico de líneas inventado
        years = [2023, 2024, 2025, 2026]
        prevalence = [28, 27.5, 27, 26.3]

        fig, ax = plt.subplots()
        ax.plot(years, prevalence, marker="o")
        ax.set_title("Disminución Proyectada de Anemia (%)")
        ax.set_xlabel("Año")
        ax.set_ylabel("Prevalencia (%)")
        st.pyplot(fig)

    elif viz_menu == "Factores Relacionados":
        st.subheader("Factores Relacionados")

        # Tabla bonita inventada
        data = {
            "Factor": ["Deficiencia de Hierro", "Malnutrición", "Enfermedades Crónicas"],
            "Impacto Relativo (%)": [40, 30, 20],
            "Relevancia": ["Alta", "Alta", "Media"]
        }

        df = pd.DataFrame(data)
        st.table(df)

elif menu == "Conclusiones":
    st.title("Conclusiones")
    st.write("Aquí puedes listar las principales ideas obtenidas a partir del análisis!")

elif menu == "Equipo":
    st.title("Equipo")
    st.write("Coloca los nombres del equipo y roles aquí si lo necesitas.")
