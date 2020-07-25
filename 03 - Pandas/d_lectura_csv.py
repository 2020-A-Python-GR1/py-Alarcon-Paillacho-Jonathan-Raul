# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:08:15 2020

@author: Familia
"""

import pandas as pd
import os
#Para leer el archivo

path = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.csv"

df1 = pd.read_csv( path, nrows = 10 )

columnas = ['id','artist','title','medium','year','height','width','units']

df2 = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas)


df3 = pd.read_csv(
    path,
    nrows = 10,
    usecols = columnas,
    index_col= 'id' )


#Para guardar los datos en un nuevo archivo
path = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.csv"







