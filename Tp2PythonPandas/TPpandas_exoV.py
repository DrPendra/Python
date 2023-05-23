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

emissions=df.iloc[:,2:].copy().sum(axis=1)
print(emissions)
copy=df_city.replace(to_replace=np.nan, value=float(0), regex=True)
df_c=df.insert(column='emissions', value=emissions,loc='INSEE commune')
#left=emissions.join(df, how='left')
inner=df_c.join(copy, how='inner')
inner.replace(to_replace=np.nan, value=float(0), regex=True)
inner.plot(kind="bar", x='NBPERSMENFISC16', y='emissions')


