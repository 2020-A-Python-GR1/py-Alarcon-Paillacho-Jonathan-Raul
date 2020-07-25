# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:48:20 2020

@author: Familia
"""


import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

#Voy a tomar una columna
s1 = df1[0]

s2 = df1[1]

s3 = df1[2]


# De esta manera se agrega una nueva columna al DataFrame con nuevos valores
df1[3] = s1


# Y así podemos trabajar con las otras columnas
df1[4] = s1 * s2 

datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'])


datos_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Jonathan',
        'Alarcón'])

series_peso = datos_fisicos_dos['Peso (kg)']
datos_jonathan = series_peso['Jonathan']
print(series_peso)
print(datos_jonathan)

df1.index = ['Jonathan','Alarcón']
df1.index = ['Dayana','Rodriguez']
df1.columns = ['a','b','c','d','e']






























