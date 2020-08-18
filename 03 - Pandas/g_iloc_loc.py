# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:02:18 2020

@author: Familia
"""


import pandas as pd

path_guardado = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.pickle"

df = pd.read_pickle(path_guardado)

primero = df.loc[1035]

print(primero)
print(primero['artist'])
print(primero.index)


serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index) # Indices son los Indices 


# Filtrado por índice, para sacar de manera horizontal
df_1035 = df[df.index == 1035]

segundo = df.loc[1035] # Filtrar por índice (1)
segundo = df.loc[[1035,1036]] #Filtrar por arr de indices (2)
segundo = df.loc[df.index == 1035] #Filtrar por arreglo de V and F

segundo = df.loc[3:5] # Filtrando desde x índice 
                      # Hasta y indice



segundo = df.loc[1035, 'artist'] # 1 Indice
segundo = df.loc[1035, ['artist', 'medium']] # Varios indices


#print(df.loc[0])


#ILOC 

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]


tercero = df.iloc[0:10, 0:4] # Filtrado indices
                             # Por rango de indice 0:4


#####################################

# Clase 15/08/2020

datos = {
    "nota 1":{
        "Pepito":7,
        "Juanita":8,
        "Maria":9
        },
     "nota 2":{
        "Pepito":3,
        "Juanita":8,
        "Maria":9
        },
    "disciplina":{
        "Pepito":8,
        "Juanita": 9,
        "Maria": 2
        },
    }

notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"] > 7
condicion_nota_dos = notas["nota 2"] > 7
condicion_disc = notas["disciplina"] > 7

mayores_siete = notas.loc[condicion_nota, ["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_disc][condicion_nota_dos]

# Para cambiar a uno
notas.loc["Maria","disciplina"] = 7

# Para cambiar a todos

notas.loc[:,"disciplina"] = 7

########################## Promedio de las 3 notas (no1 + no2 + disc) / 3 

suma_promedio = notas.loc["Maria", "disciplina"] + notas.loc["Maria", "nota 1"] + notas.loc["Maria", "nota 2"]

promedio = suma_promedio / 3 



























