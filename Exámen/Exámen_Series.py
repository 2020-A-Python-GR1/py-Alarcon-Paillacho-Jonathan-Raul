# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:29:47 2020

@author: Familia
"""


import numpy as np
import pandas as pd
import os 

#11) ¿Como crear una serie de una lista, diccionario o arreglo?


mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie1 = pd.Series(mylist)
serie1
serie2 = pd.Series(myarr)
serie2
serie3 = pd.Series(mydict)
serie3


#12) ¿Como convertir el indice de una serie en una columna de un DataFrame?

ser = pd.Series(mydict) 
# Transformar la serie en dataframe y hacer una columna indice
df1 = pd.DataFrame(ser)
df1[1] = mylist
df1.index = myarr


#13) ¿Como combinar varias series para hacer un DataFrame?

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
serie_comb = pd.concat([ser1,ser2])
df2 = pd.DataFrame(serie_comb)


#14) ¿Como obtener los items que esten en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
resp = set(ser1) - set(ser2)
resp


#15) ¿Como obtener los items que no son comunes en una serie A y serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


#16) ¿Como obtener el numero de veces que se repite un valor en una serie?

serie4 = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print(serie4.value_counts())


#17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
serie5 = pd.Series(np.random.randint(1, 5, [12]))


#18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
serie6 = pd.Series(np.random.randint(1, 10, 35))
#shape(7,5)
df3 = pd.DataFrame(serie6)


#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
serie7 = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
print(serie7[pos[0]])
print(serie7[pos[1]])
print(serie7[pos[2]])
print(serie7[pos[3]])
print(serie7[pos[4]])



#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
serie8 = pd.Series(range(5))
serie9 = pd.Series(list('abcde'))
df4 = pd.DataFrame(serie8)
df4[1] = serie9


#21)¿Obtener la media de una serie agrupada por otra serie?
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print("\n\n")
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

#data_group = pd.groupby()




#22)¿Como importar solo columnas especificas de un archivo csv?

path = "C:\\Users\\Familia\\Documents\\GitHub\\py-Alarcon-Paillacho-Jonathan-Raul\\Exámen\\BostonHousing.csv"

df5 = pd.read_csv(path, nrows=10)

columnas = ['crim', 'zn', 'chas']

df_seleccion = pd.read_csv(path,nrows=15, usecols=columnas)

















