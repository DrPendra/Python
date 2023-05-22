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

uniondf=pd.concat([df, df_city])

'''
@jit(target_backend='cuda')
def foncb(uniondf):
    for i in range(0, len(uniondf.axes[1])):
        for j in range(2, len(uniondf.axes[0])):
            if type(uniondf.iloc[j, i]) != type(0.0):
                uniondf.iloc[j, i] = 0.0
            uniondf.iloc[j, i] = float(uniondf.iloc[j, i])
    print(uniondf)
foncb(uniondf)
'''
print(uniondf)
print(uniondf.shape)
print(df.shape)
print(df_city.shape)
res=uniondf.groupby('INSEE commune').nunique()
print(res)
res2=df_city.groupby('LIBGEO').nunique()
print(res2)
res3=res2
obs= res3[(df_city['CODGEO']>1)].count()
print(res3)
print(res2.sort_value(ascending=True))
