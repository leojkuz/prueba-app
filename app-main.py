import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import reveal_slides as rs
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from tqdm import tqdm
from folium.plugins import MarkerCluster
import  streamlit_toggle as tog
import random
from matplotlib.patches import Wedge
import numpy as np

# Configuración inicial de la página
st.set_page_config(page_title="Análisis Global de la Anemia", layout="wide")

# Colocar el logo de la universidad en la parte superior
st.sidebar.image("imagenes/escudo-unalm.png", use_container_width=True)
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
        options=["Situación Global", "Análisis geográfico", "Proyecciones", "Factores Relacionados"],
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
                    text="<span style='font-size:26px; color:#1f77b4; font-family:Roboto;'><b>🌎 Prevalencia Histórica de Anemia infantil (2000-2019) 🩸</b></span>",
                    x=0.12 # Centrar el título
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
            fig_bar.update_layout(title="Esto no va. AAA. NO SÉ Q WEA PONER ACÁ",
                                  xaxis_title="Prevalencia (%)",
                                  yaxis_title="Países",
                                  plot_bgcolor='rgba(240,240,240,0.9)',
                                  yaxis=dict(autorange="reversed"))

            st.plotly_chart(fig_bar)

        # Cargar los datos
        st.subheader("Comparador histórico de anemia infantil para cada país")
        data_historico_pais_est = pd.read_csv("data/world_bank_anemia_paises_listo.csv")
        data_historico_pais_est['year'] = pd.to_numeric(data_historico_pais_est['year'], errors='coerce')
        data_historico_pais_est['year'] = data_historico_pais_est['year'].astype(int)

        # Obtener la lista de países únicos
        countries = sorted(data_historico_pais_est['pais'].unique())


        # Asignar un color único a cada país
        def assign_colors(countries):
            colors = {}
            for country in countries:
                # Asignamos un color aleatorio a cada país
                colors[
                    country] = f'rgba({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)}, 0.8)'
            return colors


        colors = assign_colors(countries)


        # Función para completar los años faltantes y hacer líneas continuas
        def completar_anios(data, country):
            # Filtrar datos del país
            country_data = data[data['pais'] == country].copy()

            # Generar el rango completo de años
            all_years = pd.DataFrame({'year': range(country_data['year'].min(), country_data['year'].max() + 1)})

            # Unir con los datos originales y llenar los valores faltantes mediante interpolación
            completed_data = pd.merge(all_years, country_data, on='year', how='left')
            completed_data['prevalencia (%)'] = completed_data['prevalencia (%)'].interpolate()

            # Añadir el nombre del país
            completed_data['pais'] = country
            return completed_data


        # Función para graficar prevalencias históricas basadas en los países seleccionados
        def plot_selected_countries_plotly(countries_selected):
            if not countries_selected:
                st.warning("Por favor selecciona al menos un país.")
                return

            # Crear una figura
            fig = go.Figure()

            for country in countries_selected:
                # Completar los años faltantes
                country_data = completar_anios(data_historico_pais_est, country)

                # Obtener el color para el país
                country_color = colors[country]

                # Añadir el segmento antes de 2020 (línea continua)
                fig.add_trace(
                    go.Scatter(
                        x=country_data['year'],
                        y=country_data['prevalencia (%)'],
                        mode='lines+markers',
                        name=country,
                        hovertemplate="Prevalencia: %{y:.2f}<extra></extra>",
                        # Personalizar el tooltip sin el símbolo '%'
                        line=dict(color=country_color)  # Usamos el color del país
                    )
                )

                # Colocar el nombre del país ligeramente desplazado a la derecha
                year_2019_data = country_data[country_data['year'] == 2019]
                if not year_2019_data.empty:
                    # Obtenemos el valor de prevalencia para 2019
                    prev_2019 = year_2019_data['prevalencia (%)'].values[0]
                    fig.add_annotation(
                        x=2019 + 1.2,  # Desplazamos un poco a la derecha de 2030
                        y=prev_2019,
                        text=country,
                        showarrow=False,
                        font=dict(size=10, color='black'),
                        xanchor='left',  # Alineación del texto a la izquierda
                        align='left'  # Alineación del texto a la izquierda
                    )

            # Ajustar el diseño del gráfico
            fig.update_layout(
                title={
                    'text': 'Prevalencia histórica de anemia',
                    'x': 0.5,  # Centrar el título
                    'xanchor': 'center',  # Asegurar que el anclaje sea en el centro
                },
                xaxis=dict(
                    title=None,  # Quitar el título del eje X
                    tickangle=-90,
                    showline=True,
                    linecolor='black',
                    ticks='outside',  # Mostrar marcas de graduación principales hacia el exterior
                    tickwidth=1,  # Grosor de las marcas de graduación
                    tickvals=list(
                        range(
                            data_historico_pais_est['year'].min(),
                            data_historico_pais_est['year'].max() + 1
                        )
                    )  # Asegurar que todos los años estén en el eje X
                ),
                yaxis=dict(
                    showline=True,  # Mostrar la línea del eje Y
                    linewidth=1,  # Definir el grosor de la línea
                    linecolor='black'  # Definir el color de la línea
                ),
                showlegend=True,
                legend_title='Países',
                yaxis_title='Prevalencia (%)',
                template='plotly_white',
                width=850  # Ampliar el ancho del gráfico,
            )

            # Mostrar el gráfico en Streamlit
            st.plotly_chart(fig)


        # Crear checkbox para seleccionar países
        selected_countries = st.multiselect('Selecciona los países', countries)

        # Actualizar y mostrar gráfico dinámicamente según selección de países
        if selected_countries:
            plot_selected_countries_plotly(selected_countries)
        else:
            st.warning("Por favor selecciona al menos un país.")
        # Cargar los datos
        # Cargar los datos
        data_ind_anemia = pd.read_csv("data/dhs_anemia_final.csv")

        # Limpiar y renombrar columnas
        data_ind_anemia.drop(data_ind_anemia.columns[[3, 4, 5, 6, 7, 8, 9, 10]], axis=1, inplace=True)
        data_ind_anemia.rename(
            columns={
                'Valor Cualquier': 'Valor Real',
                'Valor Severo': 'Valor Severo',
                '# Encuestas (sev, sin ponderar)': 'Encuestas Sin Ponderar',
                '# Encuestas (sev, ponderadas)': 'Encuestas Ponderadas',
            },
            inplace=True
        )


        # Crear la Gauge con Plotly
        def create_gauge(value, country):
            """
            Crear un velocímetro circular estilizado con Plotly y una flecha personalizada.
            """
            if value < 20:
                estado = "Anemia leve"
            elif 20 <= value < 40:
                estado = "Anemia moderada"
            else:
                estado = "Anemia alta"
            # Crear la figura base del gauge
            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=value,
                    title={'text': f"<b>{estado}</b>", 'font': {'size': 20, 'color': "white"}},
                    gauge={
                        'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "#000"},
                        'bar': {'color': "#295491"},  # Barra roja
                        'steps': [
                            {'range': [0, 20], 'color': "#32CD32"},  # Verde
                            {'range': [20, 40], 'color': "#FFD700"},  # Amarillo
                            {'range': [40, 100], 'color': "#FF4D4D"},  # Rojo
                        ],
                        'threshold': {
                            'line': {'color': "black", 'width': 4},
                            'thickness': 0.85,
                            'value': value  # Dónde apunta la aguja
                        }
                    }
                )
            )

            # Calcular la posición de la flecha en coordenadas polares
            angle = (value / 100) * 180  # Convertir el valor a un ángulo en grados
            angle_rad = np.radians(angle)  # Convertir a radianes
            radius = 0.8  # Longitud de la flecha (relativa al radio del gauge)
            x_center, y_center = 0.5, 0  # Centro del gauge (en coordenadas normalizadas)
            x_arrow = x_center + radius*np.cos(np.pi - angle_rad)
            y_arrow = y_center + radius*np.sin(np.pi - angle_rad)

            fig.add_trace(go.Scatter(
                x=[x_center, x_arrow],
                y=[y_center, y_arrow],
                mode="markers+text",
                name="Markers and Text",
                text=[(x_center, x_arrow), (y_center, y_arrow)],
                textposition="bottom center"
            ))

            # Agregar la flecha al gráfico
            fig.add_shape(
                type="line",
                x0=x_center, y0=y_center,
                x1=x_arrow, y1=y_arrow,
                line=dict(color="white", width=4)
            )

            # Configuración del diseño
            fig.update_layout(
                height=300,  # Altura del gráfico
                width=300,
                margin=dict(t=50, b=50, l=50, r=50),  # Márgenes compactos
                font=dict(color="white", family="Arial"),  # Estilo tipográfico (limpio)
                xaxis=dict(scaleanchor="y"),  # Vincular la escala del eje X con el eje Y

            )
            # Mostrar cuadrícula para facilitar el debug
            fig.update_xaxes(range=[0, 1], zeroline=False, showgrid=False)  # Fijar rango del eje X
            fig.update_yaxes(range=[0, 1], zeroline=False, showgrid=False)  # Fijar rango del eje Y
            return fig


        # Sidebar interactivo para seleccionar el país
        st.subheader("Análisis de Anemia")
        pais_seleccionado = st.selectbox("Selecciona un país:", data_ind_anemia["Pais"].unique())

        # Datos del país seleccionado
        if pais_seleccionado:
            st.title(f"Prevalencia de Anemia en {pais_seleccionado}")

            # Filtrar datos del país
            data_paises = data_ind_anemia[data_ind_anemia["Pais"] == pais_seleccionado]

            # Obtener el valor más reciente de "Valor Real"
            latest_year = data_paises["Year"].max()
            valor_real = data_paises[data_paises["Year"] == latest_year]["Valor Real"].values[0]

            # Gauge para el valor actual
            st.plotly_chart(create_gauge(valor_real, pais_seleccionado), use_container_width=True)

            # Tabla bonita con Streamlit
            st.subheader("Detalles por Año")
            st.dataframe(data_paises.style.format({
                "Year": "{:.0f}",
                "Valor Real": "{:.2f}%",
                "Valor Severo": "{:.2f}%",
            }).background_gradient(cmap="Reds", subset=["Valor Real", "Valor Severo"])
                         .set_properties(**{"text-align": "center"}))  # Centrar contenido de la tabla


    elif viz_menu == "Análisis geográfico":
        # Lectura del archivo csv de prevalencia de anemia para país y continente
        data_country = pd.read_csv("data/world_bank_continentes.csv")

        col1, col2, col3 = st.columns([1.15, 0.1, 1.75])

        with col1:
            st.subheader("Veamos la situación de la anemia infantil en cada año 🌍👀")
            anio = st.slider("Seleccione un año para visualizar", 2000, 2019, 2019)
            # Filtrar los datos para el año seleccionado
            data_filtrada = data_country[data_country['date'] == anio]

            # Ordenar por el valor de anemia y seleccionar los 10 primeros
            top_10 = data_filtrada.nlargest(10, 'value')

            # Crear el gráfico con Plotly Go
            fig = go.Figure()

            # Agregar barras al gráfico
            fig.add_trace(
                go.Bar(
                    x=top_10['country.value'],
                    y=top_10['value'],
                    marker=dict(color='indianred'),
                    text=top_10['Continente'],  # Mostrar el continente al pasar el mouse
                    textposition="outside",
                    hovertemplate="<b>País:</b> %{x}<br>" +
                                  "<b>Porcentaje de Anemia:</b> %{y}%<br>" +
                                  "<b>Continente:</b> %{text}<extra></extra>"
                )
            )

            # Configurar el diseño del gráfico
            fig.update_layout(
                title=f"Top 10 países con mayor anemia infantil en {anio}",
                xaxis=dict(title="País", tickangle=-45),
                yaxis=dict(title="Porcentaje de Anemia", range=(0, 101)),
                template="plotly_white",
                title_font=dict(size=20),
                margin=dict(l=40, r=40, t=60, b=40),
                height=600
            )

            # Mostrar el gráfico
            st.plotly_chart(fig)

        with col3:
            st.subheader(f"¿Cómo la anemia infantil ha afectado a cada contintente en {anio}?")
            with st.form(key='myform', border=False):
                # Mapa 1: Anemia por Continentes
                # Crear diccionario sobre continentes

                data_recent = data_country.loc[data_country.groupby("Continente")["date"].idxmax()]
                continent_stats = (
                    data_country[data_country["date"] == anio]
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


                # Mostrar el mapa en Streamlit
                # Mapa 1: Continentes
                mapa1 = m1
                st_folium(mapa1, width=900)
                # Esconder el boton
                hide_button_style = """
                    <style>
                    button[data-testid="stBaseButton-secondaryFormSubmit"] {
                        visibility: hidden;
                    }
                    </style>
                """
                st.markdown(hide_button_style, unsafe_allow_html=True)
                submit_button = st.form_submit_button(label="",
                                                      disabled=True)
                if submit_button: pass

        st.subheader("Ahora un vistazo más completo en cada país")
        # Mapa 2: Países
        # Se mostrará como HTML debido a que Streamlit-folium no tiene compatibilidad con MarkerCluster
        # Además no es necesario la interacción dinámica con el usuario por lo que el HTML es suficiente
        tog = tog.st_toggle_switch(label="Mostrar datos totales",
                             key="Key1",
                             default_value=False,
                             label_after=False,
                             inactive_color='#D3D3D3',
                             active_color="#D3D3D3",
                             track_color="#29B5E8"
                             )
        if tog:
            with open("data/mapa_pais.html", 'r') as f:
                html_data = f.read()
                st.components.v1.html(html_data, width=1200, height=700)
        else:
            with open("data/mapa_prevalencia_max_min.html", 'r') as f:
                html_data = f.read()
                st.components.v1.html(html_data, width=1200, height=700)

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


