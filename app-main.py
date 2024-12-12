import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import reveal_slides as rs
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from sklearn.linear_model import LinearRegression
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
        st.write("### Un análisis más detallado de la situación global e histórica de la anemia infantil")
        st.write("### Indicadores de resumen en 2019")

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

        col1, col2 = st.columns([1.2, 0.8])
        with col1:
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

        with col2:
            # Cargar los datos
            data_ind_anemia = pd.read_csv("data/dhs_anemia_final.csv")

            # Limpiar y renombrar columnas
            data_ind_anemia.drop(data_ind_anemia.columns[[3, 4, 6, 7, 9, 10, 12, 13]], axis=1, inplace=True)
            data_ind_anemia.rename(
                columns={
                    'Valor Cualquier': 'Valor General',
                    'Year': 'Año'
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
                        mode="gauge",
                        value=value,
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
                unit = np.array([np.cos(np.pi-angle_rad), np.sin(np.pi-angle_rad)])
                ro = 0.9
                ri = 0
                ax, ay = ri * unit
                x, y = ro * unit

                # Agregar la flecha al gráfico
                fig.add_annotation(
                    ax=ax,
                    ay=ay,
                    axref='x',
                    ayref='y',
                    x=x,
                    y=y,
                    xref='x',
                    yref='y',
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=4,
                    arrowcolor="#e3e7e8"
                )

                fig.add_annotation(
                    ax=ax,
                    ay=ay,
                    axref='x',
                    ayref='y',
                    x=x,
                    y=y,
                    xref='x',
                    yref='y',
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=4,
                    arrowcolor="#e3e7e8"
                )

                fig.add_trace(
                    go.Scatter(
                        x=[x], y=[y],  # Coordenadas ficticias para hover centralizado
                        mode="markers",
                        marker=dict(size=1, opacity=0),
                        hoverinfo="text",  # Muestra solo texto definido en hovertext
                        hovertext=f"<b>{estado}</b><br>Prevalencia: {value}%"
                    )
                )


                # Configuración del diseño
                fig.update_layout(
                    height=300,  # Altura del gráfico
                    margin=dict(t=70, b=10, l=70, r=70),  # Márgenes compactos
                    font=dict(color="white", family="Arial"),  # Estilo tipográfico (limpio)
                    xaxis={'showgrid': False, 'showticklabels': False, 'range': [-1, 1]},
                    yaxis={'showgrid': False, 'showticklabels': False, 'range': [0, 1]},

                )
                # Mostrar cuadrícula para facilitar el debug
                fig.update_yaxes(
                    scaleanchor="x",
                    scaleratio=1,
                )
                return fig


            # Sidebar interactivo para seleccionar el país
            st.subheader("Reportes de la gravedad de anemia infantil")
            pais_seleccionado = st.selectbox("Selecciona un país:", data_ind_anemia["Pais"].unique())

            # Datos del país seleccionado
            if pais_seleccionado:
                st.subheader(f"Prevalencia de anemia general en {pais_seleccionado} según el reporte más reciente")

                # Filtrar datos del país
                data_paises = data_ind_anemia[data_ind_anemia["Pais"] == pais_seleccionado].reset_index(drop=True)

                # Obtener el valor más reciente de "Valor Real"
                latest_year = data_paises["Año"].max()
                valor_real = data_paises[data_paises["Año"] == latest_year]["Valor General"].values[0]

                # Gauge para el valor actual
                st.plotly_chart(create_gauge(valor_real, pais_seleccionado), use_container_width=True)
                st.markdown(f"""
                    <div style="text-align: center; margin-left: 35px; margin-top: -30px; margin-bottom: -20px;">
                        <h2 style='color: white; display: inline-block;'>{valor_real}%</h2>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                            <div style="text-align: center; margin-left: 35px; margin-top: -20px; margin-bottom: -20px;">
                                <h3 style='color: white; display: inline-block;'>{pais_seleccionado}</h3>
                            </div>
                                """, unsafe_allow_html=True)

                # Tabla bonita con Streamlit
                st.subheader("Reportes de gravedad por año")
                st.dataframe(data_paises.style.format({
                    "Año": "{:.0f}",
                    "Valor General": "{:.2f}%",
                    "Valor Leve": "{:.2f}%",
                    "Valor Moderado": "{:.2f}%",
                    "Valor Severo": "{:.2f}%"
                }).background_gradient(cmap="YlOrRd", vmin=0, vmax=60,
                                       subset=["Valor Leve", "Valor Moderado", "Valor Severo"])
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
        c1, c2 = st.columns([1.4, 0.6])
        with c1:
            st.markdown("""
            # 🌍 Estimaciones Futuras: Mirando hacia el 2030
    
            El análisis de datos históricos no solo nos permite comprender lo que ha sucedido, sino que también nos da las herramientas necesarias para **proyectar escenarios futuros**. Al observar cómo han evolucionado los niveles globales de anemia infantil en el pasado, es posible extrapolar esas tendencias para anticipar qué rumbo podrían tomar las próximas décadas.
    
            La capacidad de realizar estas estimaciones no es trivial. La posibilidad de **predecir escenarios futuros**, por simplificados que sean, ofrece una base importante para:
            - **Planificación preventiva:** Si entendemos cómo podría comportarse la prevalencia según las tendencias actuales, es más fácil priorizar estrategias a largo plazo.
            - **Asignación de recursos:** Países con falta de progreso podrían recibir atención focalizada para cambiar su trayectoria.
            - **Creación de políticas públicas:** Las proyecciones generan argumentos sólidos para justificar acciones inmediatas en salud pública.
    
            El siguiente gráfico, presenta datos a comparar que muestra:
            1. Los datos históricos disponibles desde el año 2000 hasta el 2019.
            2. Una extrapolación proyectada de esos patrones basada en tendencias observadas, extendiendo el análisis hasta el 2030.
            """)

            # Cargar los datos históricos
            data_historico_est = pd.read_csv("data/world_bank_anemia_mundial_listo.csv")

            # Ordenamos los datos por año de forma ascendente (aseguramos que estén en orden cronológico)
            data_historico_est = data_historico_est.sort_values(by='year', ascending=True)

            # Calcular el factor de crecimiento promedio (promedio de las variaciones porcentuales año tras año)
            factor_crecimiento = (data_historico_est[
                                      'prevalencia (%)'].pct_change().mean() + 1)  # Para que sea un factor de multiplicación

            # Lista para almacenar los datos con las estimaciones proyectadas
            datos_con_estimaciones = []

            # Agregar los datos originales al conjunto de datos de estimaciones
            for _, row in data_historico_est.iterrows():
                datos_con_estimaciones.append({
                    'year': row['year'],
                    'nivel geográfico': row['nivel geográfico'],  # Usar nivel_geografico
                    'prevalencia (%)': row['prevalencia (%)']
                })

            # Proyectar valores desde 2020 hasta 2030 usando el factor de crecimiento
            ultima_prevalencia = data_historico_est['prevalencia (%)'].iloc[-1]  # Último valor conocido (2019)

            # El último valor de 'nivel_geografico' será el mismo en las proyecciones
            nivel_geografico = data_historico_est['nivel geográfico'].iloc[0]

            for year in range(2020, 2031):
                ultima_prevalencia *= factor_crecimiento  # Aplicar el factor de crecimiento
                datos_con_estimaciones.append({
                    'year': year,
                    'nivel geográfico': 'Mundial',  # Mantener el mismo nivel_geografico
                    'prevalencia (%)': ultima_prevalencia
                })

            # Convertir los datos con estimaciones a un DataFrame
            data_historico_est = pd.DataFrame(datos_con_estimaciones)

            # Reordenar las columnas para que aparezcan como 'year', 'prevalencia (%)' y 'nivel_geografico'
            data_historico_est = data_historico_est[['year', 'prevalencia (%)', 'nivel geográfico']]
            # Crear el gráfico de líneas interactivo con Plotly
            fig = go.Figure()

            # Agregar la línea de datos históricos al gráfico
            fig.add_trace(go.Scatter(
                x=data_historico_est[data_historico_est['year'] < 2020]['year'],
                y=data_historico_est[data_historico_est['year'] < 2020]['prevalencia (%)'],
                mode='lines+markers',
                name='Datos Históricos',
                line=dict(color='#636efa', width=3, shape='spline'),  # Agregamos 'spline' para suavizar la línea
                marker=dict(size=7, color='#636efa', symbol='circle', line=dict(color='white', width=2)),
                hovertemplate="<b>Año:</b> %{x}<br><b>Prevalencia:</b> %{y:.2f}%<extra></extra>"
            ))
            # Agregar la interseccion
            fig.add_trace(go.Scatter(
                x=data_historico_est[(data_historico_est['year'] >= 2019) & (data_historico_est['year'] <= 2020)]['year'],
                y=data_historico_est[(data_historico_est['year'] >= 2019) & (data_historico_est['year'] <= 2020)]['prevalencia (%)'],
                mode='lines+markers',
                name='Datos Históricos',
                line=dict(color='#636efa', width=3, shape='spline'),  # Agregamos 'spline' para suavizar la línea
                marker=dict(size=7, color='#636efa', symbol='circle', line=dict(color='white', width=2)),
                hoverinfo="skip",
                showlegend=False
            ))

            # Agregar la línea de datos proyectados al gráfico
            fig.add_trace(go.Scatter(
                x=data_historico_est[data_historico_est['year'] >= 2020]['year'],
                y=data_historico_est[data_historico_est['year'] >= 2020]['prevalencia (%)'],
                mode='lines+markers',
                name='Proyección',
                line=dict(color='#EF553B', width=3, dash='dot'),  # Línea punteada para diferenciar los proyectados
                marker=dict(size=7, color='#EF553B', symbol='diamond', line=dict(color='white', width=2)),
                hovertemplate="<b>Año:</b> %{x}<br><b>Proyección:</b> %{y:.2f}%<extra></extra>"
            ))

            # Personalización del diseño general
            fig.update_layout(
                title=dict(
                    text="<span style='font-size:24px; color:#1f77b4; font-family:Arial;'><b>📉 Estimación Futura de Anemia Infantil (2000-2030)</b></span>",
                    x=0.2),
                xaxis=dict(
                    title="Año",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    tickmode="linear",
                    tickangle=45,  # Rotar los ticks para mayor claridad
                    range=[1999.5, 2030.5],  # Desde justo antes del 2000 hasta 2030
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                yaxis=dict(
                    title="Prevalencia (%)",
                    title_font=dict(size=16, color='black'),
                    tickfont=dict(size=14, color='black'),
                    range=[25, 50],  # Ajustar el rango según los datos observados
                    showline=True,
                    linewidth=2,
                    linecolor='gray',
                    gridcolor='lightgray'
                ),
                plot_bgcolor='rgba(240,240,240,0.95)',  # Fondo claro para el gráfico
                paper_bgcolor='white',
                margin=dict(t=100, b=100, l=80, r=80),
                legend=dict(
                    orientation="h",  # Leyenda en formato horizontal
                    yanchor="bottom",
                    y=-0.2,
                    xanchor="center",
                    x=0.5,
                    title=None  # Ocultar encabezado "Legend"
                )
            )

            # Mejorar interactividad
            fig.update_traces(marker_line_width=1.5)
            fig.update_layout(
                hovermode="x",  # Mostrar tooltip alineado a los valores en X
                template="simple_white"
            )
            # Leyenda
            fig.update_layout(
                legend=dict(
                    orientation="v",  # Leyenda en formato vertical
                    yanchor="top",  # Alinear la parte superior con el margen
                    y=1,  # Mantener la posición de la leyenda en la parte superior
                    xanchor="left",  # Anclar al lado izquierdo
                    x=1.02,  # Empujar la leyenda fuera de la gráfica (a la derecha)
                    font=dict(
                        size=12,  # Ajustar tamaño de la fuente
                        color="black"  # Establecer el color de la fuente como negro
                    ),
                    bordercolor="gray",  # (opcional) Borde alrededor de la leyenda para resaltarla
                    borderwidth=1  # Ancho del borde de la leyenda (opcional)
                )
            )
            # Mostrar el gráfico en Streamlit
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
                ## 🌎 Comparador de Países: Análisis Futuro

                En esta sección, hemos adaptado el gráfico interactivo presentado en el capítulo anterior, que permitía comparar la prevalencia de anemia infantil entre diferentes países hasta el año 2019.
                Ahora, este gráfico no solo sigue permitiendo la selección y comparación de múltiples países, sino que también **incorpora las proyecciones calculadas para cada uno**, basándonos en las tendencias estimadas. Esta extensión resulta esencial para evaluar cómo podrían afectar los patrones globales y locales a cada región, permitiéndonos identificar posibles diferencias entre naciones en el futuro cercano.
                """)

            st.markdown("""
            ## 📊 Reflexiones sobre los Datos y Proyecciones
    
            El análisis de los datos históricos revela un comportamiento importante: si bien la prevalencia global de la anemia infantil ha mostrado una **tendencia decreciente desde los años 2000**, esta mejora ha ocurrido a un ritmo **moderado a lento**. Este hecho es significativo porque refleja que, aunque existen avances globales en nutrición y desarrollo infantil, estos no han sido lo suficientemente acelerados como para lograr una reducción más sustancial.
    
            #### Puntos Clave:
            1. **Tendencia General:** La prevalencia promedio a nivel mundial ha disminuido desde niveles cercanos al 45% en el año 2000 hasta valores alrededor del 35% al cierre del 2019 (según los datos históricos). Sin embargo, esta reducción representa menos del 1% anual en promedio.
            
            2. **Proyección Futura:** El modelo predictivo sugiere que, si las condiciones observadas en las últimas dos décadas permanecen constantes, el porcentaje global podría alcanzar valores cercanos al 35% para el año 2030. Aunque esto indica una mejora progresiva en términos absolutos, podría argumentarse que el ritmo no es lo suficientemente acelerado para cumplir objetivos globales más ambiciosos.
            
            3. **Limitaciones del Análisis:** Es crucial tener presente que las proyecciones aquí expuestas asumen que las tendencias pasadas continuarán inalteradas. Factores disruptivos —por ejemplo, pandemias globales o intervenciones masivas— podrían cambiar radicalmente las trayectorias proyectadas.
            
            #### Conclusión:
            El principal aprendizaje extraído de este análisis es que los esfuerzos por combatir la anemia infantil globalmente han tenido un impacto positivo pero **marginal** en términos estadísticos. El descenso observado en las últimas dos décadas da lugar a una tendencia predecible pero insuficiente para la eliminación total del problema a mediano plazo.
            
            Este comportamiento resalta la importancia de continuar monitoreando indicadores clave y ajustar periódicamente estos modelos predictivos utilizando información actualizada. De esta manera, se pueden construir escenarios futuros más dinámicos que reflejen mejor los contextos globales cambiantes.
    
            """)




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


