print('---Exercice A---')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download
from numba import jit, cuda

df = pd.read_csv("IGT - Pouvoir de réchauffement global.csv", sep=",")

df_city = pynsee.download.download_file("FILOSOFI_COM_2016")
meta = pynsee.get_file_list()

meta = pynsee.get_file_list()
meta.loc[meta['label'].str.contains(r"Filosofi.*2016")]

print(df)
dep= df["INSEE commune"].copy()
for i in range(len(dep)):
    dep[i]= dep[i][0:2]
df.insert(0, 'departement',  dep)
print(df)
print(df_city)
dep2= df_city["CODGEO"].copy()
for i in range(len(dep2)):
    dep2[i]= dep2[i][0:2]
df_city.insert(0, 'departement',  dep2)
print(df_city)
df_log = df.groupby(['departement'], as_index=False).sum()
print(df_log)
df_log2=df_city.groupby(['departement']).sum()
print(df_log2)
df_logd=df_log.drop('INSEE commune', axis=1)
df_logd.drop('Commune', axis=1, inplace=True)
df_logd.plot(kind="bar", x='departement', y='Tertiaire')
print(df_log.sort_values('Tertiaire',ascending=False)[:10])
print(df_log.sort_values('Tertiaire',ascending=False)[-5:])

print('---Exercice B---')
import timeit

df_copy=df_city.copy()
df_copy2=df.copy()
dep= df["INSEE commune"].copy()
for i in range(len(dep)):
    dep[i]= dep[i][0:2]

#df_copy2.drop(df_copy2.index(dep), inplace=True)
