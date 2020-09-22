# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:26:41 2020

@author: Familia
"""


import pandas as pd
import numpy as np
import os

path = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\Proyectos II Bimestre\\datos\\vgsales.csv"

df1 = pd.read_csv( path)

#columnas = ['id','artist','title','medium','year','height','width','units']

#df2 = pd.read_csv(
#    path,
#    nrows = 10,
#    usecols = columnas)

anio = df1['Publisher'] == "Nintendo"
print(anio.value_counts())

df_anio = df1[anio]
#arreglo = np.where(df1['Year'] == 2005 )[0]
#limite = arreglo[-1]
#df_nuevo = df1.iloc[0:limite]

serie_anio = df1['Platform']
top_vendidos = serie_anio.value_counts()[:10].index.to_list()
num = serie_anio.value_counts()[:10].values

plataforma = df_anio['Name']
top_mas_usadas = plataforma.value_counts()[:5].index.to_list()
mas_compras = plataforma.value_counts()[:5].values


anio1 = df1['Year'] == 2013
df_anio1 = df1[anio1]
ventas = df_anio1['NA_Sales'] > 5.0
df_ventas = df_anio1[ventas]
df_nombre = df_ventas['Name']
df_generos = df_ventas['Genre']


anio1 = df1['Year'] == 2000
df_anio1 = df1[anio1]
plataforma = df_anio1['Platform']
top_mas_usadas = plataforma.value_counts()[:5].index.to_list()
mas_compras = plataforma.value_counts()[:5].values

