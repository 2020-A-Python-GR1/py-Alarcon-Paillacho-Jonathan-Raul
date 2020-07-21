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


#Clase 21/07/2020

svc_cuadrado = np.square(serie_valor_ciudad)


ciudades_uno = pd.Series({
    "Montañita": 300,
    "Guayaquil": 10000,
    "Quito": 2000})

ciudades_dos = pd.Series({
    "Loja": 300,
    "Quevedo": 10000,
    "Guayaquil": 2000})


ciudades_uno["Loja"] = 0


print(ciudades_uno + ciudades_dos)

#La suma de las dos sigue siendo una serie 

print(type(ciudades_uno + ciudades_dos))

#Para agregar
ciudades_add = ciudades_uno.add(ciudades_dos)

# sub()
# mul()
# div()

#Para concatenar 
#Pero de esta manera se repiten los valores
ciudad_concat = pd.concat([ciudades_uno,ciudades_dos])

ciudad_concat_verify = pd.concat([
    ciudades_uno,
    ciudades_dos],
    verify_integrity = False)

# Append es lo mismo que concat
ciudad_concat_verify = ciudades_uno.append(
    ciudades_dos,
    verify_integrity = False)



print(ciudades_uno.max()) 
print(pd.Series.max(ciudades_uno))
print(np.max(ciudades_uno))


print(ciudades_dos.min()) 
print(pd.Series.min(ciudades_dos))
print(np.min(ciudades_dos))

# Funciones estadisticas

# Media
print(ciudades_uno.mean())

# Mediana
print(ciudades_uno.median())

# Promedio
print(np.average(ciudades_uno))

# Para obtener las primeras y ultimas filas de nuestra serie
print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))


# Para ordenar de manera no ascendente
print(ciudades_uno.sort_values(
    ascending = False).head(2))

print(ciudades_uno.sort_values().tail(2))

# 0 - 1000  5%
# 1001 - 5000  10%
# 5001 - 12000  15%

def calcular(valor_serie):
    if(valor_serie <= 1000):
        return valor_serie * 1.05
    if(valor_serie > 1000 and valor_serie <= 5000):
        return valor_serie * 1.10
    if(valor_serie > 5000):
        return valor_serie * 1.15
    
ciudad_calculada = ciudades_uno.map(calcular)


# if - else

# Cuando no CUMPLE la condición, aplica lo indicado

resultado = ciudades_uno.where(ciudades_uno < 1000,
                               ciudades_uno * 1.05)




series_numeros = pd.Series(['1.0','2',-3])

print(pd.to_numeric(series_numeros))

# Tambien podemos definir lo que nosotros queremos que se transforme

print(pd.to_numeric(series_numeros , downcast= 'integer'))


series_numeros_err = pd.Series(['no tiene', '1.0', '2', -3])

# ignore , coerce, raise (default)


#print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors = 'ignore'))
print(pd.to_numeric(series_numeros_err, errors = 'coerce'))

































