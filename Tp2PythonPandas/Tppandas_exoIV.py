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
print(df_wide)
print(df_wide.iloc[:,2:].sum())
plt.figure(1)
plt.plot(df_wide.iloc[:,2:].sum())
plt.show()
print(df_wide.iloc[:,2:].sum().max())


print('---Exercice B---')

df_wide = df.copy()
df_long=df.copy()
df_long.drop('INSEE commune', inplace=True, axis=1)
df_long.drop('Commune', inplace=True, axis=1)
#df_long.astype(dtype=np.long)
dep= df["INSEE commune"].copy()
for i in range(len(dep)):
    dep[i]= dep[i][0:2]