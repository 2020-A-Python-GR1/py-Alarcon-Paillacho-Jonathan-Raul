# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:28:37 2020

@author: Familia
"""


import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

#Tipos de Archivos

# JSON
# Excel
# SQL

path_excel = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.xlsx"
path_excel_indice = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data_indice.xlsx"
path_excel_columnas = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data_column.xlsx"
#Con el índice como columna
#sub_df.to_excel(path_excel)

#Sin el índice como columna
#sub_df.to_excel(path_excel_indice, index = False)

columnas = ['artist', 'title', 'year']

#sub_df.to_excel(path_excel_columnas, columns = columnas)


# Multiples hojas de trabajo

path_excel_mt = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt, engine = 'xlsxwriter')

sub_df.to_excel(writer, sheet_name = 'Primera')

sub_df.to_excel(writer, sheet_name = 'Segunda')

sub_df.to_excel(writer, sheet_name = 'Tercera')

writer.save()

# Formato Condicional 

# Ver los artistas que tenemos dentro del df

#num_artistas = sub_df['artist'].value_counts()

path_excel_colors = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colors, engine = 'xlsxwriter')

num_artistas = sub_df['artist'].value_counts()

num_artistas.to_excel(writer, sheet_name = 'Artistas')

hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

formato_artistas = {
    "type": "2_color_scale",
    "min_value": "10",
    "min_type": "percentile",
    "max_value": "99",
    "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

writer.save()


########### SQL #####################

with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas',conexion)
    
    
##################### JSON #####################

sub_df.to_json('artistas.json')

sub_df.to_json('artistas_tabla.json', orient = 'table')





































