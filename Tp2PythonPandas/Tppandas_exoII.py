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

print(df[:10])
print(30*'*')
print(df[len(df.axes[0])-15:])
print(30*'*')
print(df.sample(n=10))
print(30*'*')
print(df.sample(frac=0.05))
print(30*'*')
print(pd.concat([df[:10], df[:10].sample(frac=1),
                 df[:10].sample(frac=1),df[:10].sample(frac=1),
                 df[:10].sample(frac=1),df[:10].sample(frac=1),
                 df[:10].sample(frac=1),df[:10].sample(frac=1),
                 df[:10].sample(frac=1),df[:10].sample(frac=1)]))
print(30*'*')
df2=df[:7]
print(30*'*')
print(df2.sample(frac=0.5))
@jit(target_backend='cuda')
def foncA(df2):
    for i in range(99):
        print(30 * '*')
        print(df2.sample(frac=0.8))
foncA(df2)

print(30*'*')
print(30*'*')

print(df_city[:10])
print(30*'*')
print(df_city[len(df_city.axes[0])-15:])
print(30*'*')
print(df_city.sample(n=10))
print(30*'*')
print(df_city.sample(frac=0.05))
print(30*'*')
print(pd.concat([df_city[:10], df_city[:10].sample(frac=1),
                 df_city[:10].sample(frac=1),df_city[:10].sample(frac=1),
                 df_city[:10].sample(frac=1),df_city[:10].sample(frac=1),
                 df_city[:10].sample(frac=1),df_city[:10].sample(frac=1),
                 df_city[:10].sample(frac=1),df_city[:10].sample(frac=1)]))
print(30*'*')
df2_city=df_city[:7]
print(30*'*')
print(df2_city.sample(frac=0.5))
@jit(target_backend='cuda')
def foncA(df2):
    for i in range(99):
        print(30 * '*')
        print(df2.sample(frac=0.8))
foncA(df2_city)

print(30*'*')
print(30*'*')
print(30*'*')

print('---Exercice B---')

df.replace(np.nan, 0.0, inplace=True)
df_copy=df.copy()
df_copy.drop(columns='INSEE commune',inplace=True)
df_copy.drop(columns='Commune',inplace=True)
df_copy.replace(np.nan, 0.0, inplace=True)
print(df_copy.astype(float))
print(df.shape)
df_city.replace(np.nan, 0.0, inplace=True)
dfc_copy=df_city.copy()
dfc_copy.drop(columns='CODGEO',inplace=True)
dfc_copy.drop(columns='LIBGEO',inplace=True)
print(dfc_copy.astype(float))
print(df_city.shape)
res=df.groupby('INSEE commune').nunique()
print(res)
res2=df_city.groupby('LIBGEO').nunique()
print(res2)
#Oui, elles sont coherent car si on prend les noms des communes, les grandes villes française peuvent avoir plusieur cod postal
s= df_city.groupby('LIBGEO')['CODGEO'].transform('nunique').rename('Unique counts')
x = df_city[s > 1]['CODGEO']
print(x)
print(x.astype(str).sort_values(ascending=True))
'''
@jit(target_backend='cuda')
def foncB(x):
    for i in x:
        print(df_city[df_city['CODGEO']==i]['NBPERSMENFISC16'].describe().rename(i))
foncB(x)
'''
s= df_city['NBPERSMENFISC16'].copy().astype(float)
print(s)
print(df_city[s >100000]['LIBGEO'])

s= df_city['LIBGEO'].copy()
print(df_city[s == 'Montreuil'])
print(df_city[s == 'Saint-Denis'])