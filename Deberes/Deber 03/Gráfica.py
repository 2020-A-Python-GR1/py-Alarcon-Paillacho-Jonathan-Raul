# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:42:55 2020

@author: Familia
"""


import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter

path_guardado = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\03 - Pandas\\data\\artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

num_artistas = sub_df['artist'].value_counts()

rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

workbook = xlsxwriter.Workbook('grafica_artistas.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write_column('A1', num_artistas.index)
worksheet.write_column('B1', num_artistas)

chart = workbook.add_chart({'type': 'doughnut'})

chart.add_series({
    'categories': '=Sheet1!$A$1:$A$85',
    'values':     '=Sheet1!$B$1:$B$85',
    
})


chart.set_y_axis({'name': 'Cantidad'})
chart.set_x_axis({'name': 'Artistas'})


worksheet.insert_chart('D2', chart)

workbook.close()












