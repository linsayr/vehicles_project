import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Explorador de Vehículos - USA')

# Botón para histograma
if st.button('Mostrar histograma de odómetro'):
    st.write('Creando histograma...')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Creando gráfico de dispersión entre odómetro y precio...')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
