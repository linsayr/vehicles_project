# Dashboard de análisis de vehículos en venta

Esta aplicación web interactiva fue desarrollada con Streamlit y permite explorar visualmente un conjunto de datos de anuncios de coches usados en Estados Unidos.

## ¿Qué puedes hacer?

- Ver un histograma interactivo del kilometraje (`odometer`) de los vehículos.
- Ver un gráfico de dispersión del precio vs el año del modelo, filtrado por tipo de vehículo.
- Interactuar con los elementos visuales mediante casillas de verificación.

## Estructura del proyecto

- `app.py`: Aplicación principal en Streamlit.
- `vehicles_us.csv`: Conjunto de datos con información de los vehículos.
- `notebooks/EDA.ipynb`: Análisis exploratorio inicial realizado en Jupyter Notebook.

## Cómo ejecutar

```bash
streamlit run app.py
