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

df_wide = df.copy()
df_wide.replace(to_replace=np.nan, value=float(0), regex=True, inplace=True)
df_wide.iloc[:,2:].astype('long')
print(df_wide)
print(df_wide.iloc[:,2:].sum())
plt.figure(1)
plt.plot(df_wide.iloc[:,2:].sum())
plt.show()
print(df_wide.iloc[:,2:].sum().max())


print('---Exercice B---')

df_wide = df.copy()
df_wide.replace(to_replace=np.nan, value=float(0), regex=True, inplace=True)
df_wide.iloc[:,2:].astype('long')
dep= df["INSEE commune"].copy()
for i in range(len(dep)):
    dep[i]= dep[i][0:2]
f=df_wide.iloc[:,2:].sum(axis=1)
print(df_wide['Commune']+'    '+str(f))
print(f.describe())