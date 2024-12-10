import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import reveal_slides as rs
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from tqdm import tqdm
from folium.plugins import MarkerCluster

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
    # Noticias de la anemia en el mundo
    ---
    ## País 1: Brasil 🌴
    --
    
    <!-- .slide: data-background-color="#283747" -->
    🌎 **Ubicación:** América del Sur
    🍖 **Cultura:** Famoso por su Carnaval y la samba.
    🏞 **Dato relevante:** Es uno de los principales productores de hierro y acero en el mundo.
    ---
    ## País 2: Japón 🗾
    --
    
    <!-- .slide: data-background-color="#283747" -->
    🎌 **Ubicación:** Asia Oriental
    🍣 **Cultura:** Punto focal de innovación tecnológica y cuna del sushi.
    🚄 **Dato relevante:** Poseen uno de los sistemas ferroviarios más veloces y precisos.
    ---
    ## País 3: Egipto 🏺
    --
    
    <!-- .slide: data-background-color="#283747" -->
    🌅 **Ubicación:** África (Noroeste)
    🕌 **Cultura:** Hogar de las pirámides y la rica historia faraónica.
    🛤 **Dato relevante:** El Nilo es la principal fuente de agua del país.
    """

    # Creación del layout con columnas
    col1, col2, col3 = st.columns([1, 2, 1])  # Relación: 1:2:1 para centrar

    with col2:  # Contenido en la columna central
        response_dict = rs.slides(content_markdown, height=500, markdown_props={"data-separator-vertical":"^--$"})

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
        # Datos ficticios
        years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
        anemia_global = [30.1, 29.8, 29.3, 28.7, 28.4, 28.1, 27.8]  # Tendencia Mundial
        countries = ['India', 'Nigeria', 'Pakistán', 'Bangladés', 'Etiopía',
                     'República del Congo', 'Sudán', 'Afganistán', 'Angola', 'Yemen']
        prevalence = [51.3, 49.2, 45.0, 44.8, 42.1, 41.3, 40.5, 39.8, 38.8, 37.3]

        # Dashboard Principal
        st.write("### Un análisis más detallado de la situación global e indicadores clave sobre la anemia infantil en 2019.")

        # Indicadores (Méritos)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(label="Prevalencia Global (%)", value="39.8%", delta="-0.5% respecto al año 2015")

        with col2:
            st.metric(label="Continente más afectado", value="Asia (???? %) Pendiente")

        with col3:
            st.metric(label="Número estimado de afectados (millones)", value="274M")

        col1, col2 = st.columns([1.9, 1.1])

        with col1:
            # Cargar los datos desde el archivo CSV
            data_historico = pd.read_csv("data/world_bank_anemia_mundial_listo.csv")

            # Crear el gráfico de líneas interactivo con Plotly
            fig = go.Figure()

            # Agregar la línea principal al gráfico
            fig.add_trace(go.Scatter(
                x=data_historico["year"],
                y=data_historico["prevalencia (%)"],
                mode='lines+markers',
                name='Prevalencia',
                line=dict(color='#636efa', width=3),
                marker=dict(size=7, color='#636efa', symbol='circle', line=dict(color='white', width=2)),
                hovertemplate="<b>Año:</b> %{x}<br><b>Prevalencia:</b> %{y:.2f}%<extra></extra>"
            ))

            fig.update_traces(line_shape='spline')

            # Personalización del diseño del gráfico
            fig.update_layout(
                title=dict(
                    text="<span style='font-size:26px; color:#1f77b4; font-family:Roboto;'><b>🌎 Prevalencia Histórica de Anemia infantil(2000-2019) 🩸</b></span>",
                    x=0.16 # Centrar el título
                ),
                xaxis=dict(
                    title="Año",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    tickmode="linear",
                    tickangle=45,  # Rotar los ticks para que no se apilen
                    range=[1999.5, 2019.5],
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                yaxis=dict(
                    title="Prevalencia (%)",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    range=[25, 50],  # Ajustar el rango según los datos
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                plot_bgcolor='rgba(240,240,240,0.95)',  # Fondo claro para el gráfico
                paper_bgcolor='white',
                margin=dict(t=100, b=100, l=80, r=80)
            )

            # Mejorar interactividad (opcional)
            fig.update_traces(marker_line_width=1.5)
            fig.update_layout(
                hovermode="x",  # Mostrar valores al pasar sobre la línea
                template="simple_white"
            )

            # Mostrar el gráfico en Streamlit (si lo necesitas)
            st.plotly_chart(fig)

        with col2:
            fig_bar = go.Figure([go.Bar(x=prevalence, y=countries, orientation='h',
                                        marker_color='indianred')])
            fig_bar.update_layout(title="Top 10 Países con Mayor Prevalencia de Anemia",
                                  xaxis_title="Prevalencia (%)",
                                  yaxis_title="Países",
                                  plot_bgcolor='rgba(240,240,240,0.9)',
                                  yaxis=dict(autorange="reversed"))

            st.plotly_chart(fig_bar)


        # Gráfico de Barras (Top 10 Países con Mayor Prevalencia de Anemia)


    elif viz_menu == "Análisis geográfico":
        st.write("Hola")

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
    st.subheader("¿Cómo la anemia infantil a afectado a cada contintente?")

    # Lectura del archivo csv de prevalencia de anemia para país y continente
    data_country = pd.read_csv("data/world_bank_continentes.csv")


    # Mapa 1: Anemia por Continentes
    def crear_mapa_por_continentes(data_country):
        if "mapa1" not in st.session_state or st.session_state.mapa1 is None:
            # Crear diccionario sobre continentes
            data_recent = data_country.loc[data_country.groupby("Continente")["date"].idxmax()]
            continent_stats = (
                data_country[data_country["date"] == 2019]
                .groupby("Continente")[["country.value", "value", "date"]]
                .apply(lambda group: pd.Series({
                    "max_prevalence_country": group.loc[group["value"].idxmax()]["country.value"],
                    "max_prevalence_value": group["value"].max(),
                    "min_prevalence_country": group.loc[group["value"].idxmin()]["country.value"],
                    "min_prevalence_value": group["value"].min()
                }))
                .reset_index()
            )

            # Coordenadas aproximadas de los continentes
            locations = {
                "Africa": [9.1, 23.7],
                "Asia": [34.0, 100.0],
                "Europe": [54.0, 15.0],
                "North America": [37.0, -98.0],
                "South America": [-15.0, -60.0],
                "Oceania": [-20.0, 130.0]
            }

            # Crear el mapa
            m1 = folium.Map(location=[0, 0], zoom_start=2)

            for _, row in continent_stats.iterrows():
                continent = row["Continente"]
                tooltip_text = f"""
                    <b>{continent}</b><br>
                    <i>País con mayor prevalencia:</i> {row['max_prevalence_country']} ({row['max_prevalence_value']}%)<br>
                    <i>País con menor prevalencia:</i> {row['min_prevalence_country']} ({row['min_prevalence_value']}%)
                """
                folium.CircleMarker(
                    location=locations[continent],
                    radius=10,
                    color="blue",
                    fill=True,
                    fill_color="blue",
                    fill_opacity=0.6,
                    tooltip=tooltip_text,
                ).add_to(m1)

            # Guardamos el mapa en session_state
            st.session_state.mapa1 = m1

        return st.session_state.mapa1


    # Mapa 2: Anemia por Países
    def crear_mapa_por_paises(data_country):
        if "mapa2" not in st.session_state or st.session_state.mapa2 is None:
            df = data_country.dropna(subset=["latitude", "longitude"])

            # Crear el mapa
            m2 = folium.Map(location=[0, 0], zoom_start=2)
            marker_cluster = MarkerCluster().add_to(m2)

            for _, row in df.iterrows():
                tooltip_text = (
                    f"País: {row['country.value']}<br>"
                    f"Año: {row['date']}<br>"
                    f"Prevalencia: {row['value']:.2f}"
                )
                folium.CircleMarker(
                    location=[row['latitude'], row['longitude']],
                    radius=10,
                    color='blue',
                    fill=True,
                    fill_color='cyan',
                    fill_opacity=0.7,
                    tooltip=tooltip_text,
                ).add_to(marker_cluster)

            # Guardamos el mapa en session_state
            st.session_state.mapa2 = m2

        return st.session_state.mapa2


    # Mostrar el mapa en Streamlit
    # Mapa 1: Continentes
    mapa1 = crear_mapa_por_continentes(data_country)
    folium_static(mapa1, width=900)

    st.subheader("Un vistazo a la anemia infantil en cada país")
    # Mapa 2: Países
    mapa2 = crear_mapa_por_paises(data_country)
    folium_static(mapa2, width=900)
