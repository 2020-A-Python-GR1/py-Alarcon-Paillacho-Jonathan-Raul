# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:45 2020

@author: Familia
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)

#tambien vamos a crear series con otros valores
series_d = pd.Series(
    [True,
    False,
    12,
    12.25,
    "Jonathan",
    None,
    (1),
    [2],
    {"Nombre": "Jonathan"}
    ])

print(series_d[4])

lista_ciudades = [
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"]

serie_de_ciudad = pd.Series(
    lista_ciudades,
    index = ["A","B","C","D"])

print(serie_de_ciudad["B"])
print(serie_de_ciudad[1])

#Serie a partir de un diccionario
valores_ciudad = {
    "Ibarra": 95000,
    "Guayaquil": 10000,
    "Cuenca": 7000
    }

serie_valor_ciudad = pd.Series(valores_ciudad)

#Vamos a filtrar
ciudades_menores_5k = serie_valor_ciudad < 9000

print(type(serie_valor_ciudad))
print(type(ciudades_menores_5k))
print(ciudades_menores_5k)

s5 = serie_valor_ciudad[ciudades_menores_5k]

serie_valor_ciudad = serie_valor_ciudad * 1.1

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Cuenca"] - 50

print("Bogota" in serie_valor_ciudad)




