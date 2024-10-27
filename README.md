# 🛒 Análisis de Precios en Supermercados de España

## 📖 Descripción
Este proyecto realiza un análisis detallado de los precios de 3 productos básicos en seis grandes supermercados en España, con datos recolectados hasta la fecha del 26-10-2024. El enfoque está en los productos de alta demanda como el aceite de girasol, aceite de oliva y leche, analizando la variabilidad y tendencias de precios en cada supermercado. Este análisis permite identificar patrones de estabilidad, fluctuaciones y posibles anomalías en los precios de estos productos esenciales.

El objetivo es facilitar la comprensión de cómo los precios fluctúan entre distintos supermercados, proporcionando una guía útil para consumidores y analistas interesados en la dinámica de precios de consumo básico.

## 🗂️ Estructura del Proyecto
├── datos/ # Datos crudos y procesados 
├── Notebooks/ # Notebooks de Jupyter con el análisis 
│ └── EDA.ipynb # Análisis Exploratorio de Datos │ 
│ └── Web_scrap.ipynb # Notebook de Web Scraping 
├── src/ # Scripts de procesamiento y modelado 
│ └──funciones.py
├── README.md # Descripción del proyecto 
└── Script-Proyecto.py # Script principal del proyecto


## 🛠️ Instalación y Requisitos
Este proyecto utiliza Python 3.8 y requiere las siguientes bibliotecas:

- pandas
- numpy
- matplotlib
- seaborn
- requests
- BeautifulSoup4

Para instalar todas las dependencias, puedes usar el siguiente comando:

```bash
pip install -r requirements.txt

## 📊 Resultados y Conclusiones

### Aceite de Girasol
Se observa que Carrefour tiene la media de precio más alta (8.51), mientras que Hipercor ofrece el precio promedio más bajo (3.46). A lo largo del tiempo, Mercadona destaca por su estabilidad, mientras que Carrefour y Hipercor presentan fluctuaciones notables, especialmente en el periodo entre julio y agosto.  
En cuanto a anomalías, Mercadona muestra muy pocas, mientras que Carrefour e Hipercor tienen más variaciones, indicando una posible estrategia de ajuste de precios en función de la demanda.

### Aceite de Oliva
Alcampo tiene el precio promedio más alto (23.27) mientras que Eroski ofrece el precio más bajo (11.30). Este producto muestra una tendencia general a la baja con algunos picos en agosto y octubre, y se destaca Hipercor por los mayores picos tanto en alzas como en descensos, mientras que Mercadona y Dia muestran menos volatilidad.  
A partir de octubre, se observan alzas generalizadas que reflejan ajustes en función de la demanda o de factores estacionales.

### Leche
Carrefour, Hipercor y Eroski mantienen precios bajos y constantes, aunque Carrefour muestra picos ocasionales. Alcampo, Dia y Mercadona presentan precios promedio más altos, lo cual podría deberse a la diversidad de presentaciones y productos dentro de la categoría.  
En términos de estabilidad, Carrefour es el más constante, mientras que Alcampo y Dia tienen un comportamiento más dinámico, con fluctuaciones de precios que reflejan un ajuste a cambios en el mercado.

### Análisis General
Este análisis destaca la competitividad y las estrategias de precios entre los supermercados. Mercadona y Carrefour ofrecen opciones estables, siendo preferibles para consumidores que buscan estabilidad en los precios. Por otro lado, Hipercor y Alcampo muestran variabilidad en sus estrategias de precios, posiblemente en respuesta a cambios en los costos y demandas de productos específicos.

## 🔄 Próximos Pasos
- Profundizar en el análisis de presentaciones y formatos de productos que puedan influir en las variaciones de precios.
- Explorar el impacto de factores externos, como promociones y campañas de marketing, en los cambios de precios.

## ✒️ Autor
- **Nelson Carvajal** - [@ngcarvajall](https://github.com/ngcarvajall)
