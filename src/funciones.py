from bs4 import BeautifulSoup
import random
# Requests
import requests
from tqdm import tqdm
import pandas as pd
import numpy as np

def obtener_url_decat_deproducto(url):
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