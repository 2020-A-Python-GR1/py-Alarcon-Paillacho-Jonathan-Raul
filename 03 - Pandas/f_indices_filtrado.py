# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:29:30 2020

@author: Familia
"""


import pandas as pd

path_guardado = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(artistas.size)
print(len(artistas))

# Con esto obtenemos de cada artista las obras que ha realizado 

blake = df['artist'] == 'Blake, William' #Esto es una serie

print(blake.value_counts())

df_blake = df[blake] # Esto sigue siendo un DataFrame 

