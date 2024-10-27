from bs4 import BeautifulSoup
import random
# Requests
import requests
from tqdm import tqdm
import pandas as pd
import numpy as np

def obtener_url_decat_deproducto(url):
    """
    Extrae las URLs de productos de una página específica de categoría.

    Esta función toma una URL de una página de categoría en un sitio web y hace una solicitud HTTP 
    para obtener su contenido. Si la solicitud es exitosa (status code 200), utiliza BeautifulSoup 
    para analizar el HTML y extraer los enlaces de productos que se encuentran dentro de elementos 
    `div` con la clase `"card h-100"`. Finalmente, devuelve una lista de estos enlaces.

    Parámetros:
    -----------
    url : str
        La URL de la página de categoría de la cual se extraerán los enlaces de productos.

    Retorna:
    --------
    list of str
        Una lista de URLs (`hrefs`) de los productos encontrados en la página de categoría.
        Si la solicitud no es exitosa, la lista devuelta estará vacía.

    """
    link = requests.get(url)
    print('Hemos hecho el requests, vamos al if')
    if link.status_code == 200:
        sopa = BeautifulSoup(link.content, "html.parser")
        lista_de_cajas = sopa.findAll('div', {'class': "card h-100"})
        lista_href = []
        for i in range(len(lista_de_cajas)):
            h_ref = lista_de_cajas[i].find("a").get('href')
            lista_href.append(h_ref)
    else:
        print(f'El status code es {link.status_code}')
    return lista_href

def obtener_url_decat_deproducto2(url):
    """
    Extrae las URLs de los enlaces de productos históricos de una página específica de categoría.

    Esta función toma una URL de una página de categoría en un sitio web y hace una solicitud HTTP 
    para obtener su contenido. Si la solicitud es exitosa (status code 200), utiliza BeautifulSoup 
    para analizar el HTML y extraer los enlaces de productos que contienen el texto 'Histórico' 
    dentro de elementos `div` con la clase `"card h-100"`. Finalmente, devuelve una lista de estos enlaces.

    Parámetros:
    -----------
    url : str
        La URL de la página de categoría de la cual se extraerán los enlaces de productos históricos.

    Retorna:
    --------
    list of str
        Una lista de URLs (`hrefs`) de los productos históricos encontrados en la página de categoría.
        Si la solicitud no es exitosa, la lista devuelta estará vacía.
    """
    link = requests.get(url)
    print('Hemos hecho el requests, vamos al if')
    if link.status_code == 200:
        sopa = BeautifulSoup(link.content, "html.parser")
        lista_de_cajas = sopa.findAll('div', {'class': "card h-100"})
        lista_href = []
        for i in range(len(lista_de_cajas)):
            if lista_de_cajas[i].find('a').text == 'Histórico':
                h_ref = lista_de_cajas[i].find("a").get('href')
                lista_href.append(h_ref)
    else:
        print(f'El status code es {link.status_code}')
    return lista_href

def scrapeo(url):
    """
    Realiza el scraping de una tabla en una página web y devuelve los datos en un DataFrame.

    Esta función toma una URL, realiza una solicitud HTTP para obtener su contenido, y si la solicitud 
    es exitosa (status code 200), utiliza BeautifulSoup para analizar el HTML y extraer los datos de 
    una tabla específica con la clase `"table table-striped table-responsive text-center"`. 
    Los datos se organizan en un DataFrame de Pandas con las columnas obtenidas de los encabezados 
    de la tabla.

    Parámetros:
    -----------
    url : str
        La URL de la página de la cual se extraerá la tabla.

    Retorna:
    --------
    pd.DataFrame
        Un DataFrame de Pandas con los datos extraídos de la tabla de la página web. Las columnas 
        del DataFrame son los encabezados de la tabla en la página web.
    """
    link = requests.get(url)
    # print('Hemos hecho el requests, vamos al if')
    if link.status_code == 200:
        sopa = BeautifulSoup(link.content, 'html.parser')
        info_sopa = sopa.find('table', {'class' :"table table-striped table-responsive text-center"} )
        columnas = info_sopa.findAll("th")
        nombre_columnas = [i.getText() for i in columnas]
        valores_columnas = info_sopa.findAll('td')
        informaciones = [i.getText() for i in valores_columnas]
        data = informaciones
        reshaped_data = np.array(data).reshape(-1, 3)
        df = pd.DataFrame(reshaped_data, columns=nombre_columnas)
        return df