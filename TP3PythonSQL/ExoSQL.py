import pandas
import matplotlib.pyplot as plt
# Importation de sqlalchemy autre ORM
from sqlalchemy import create_engine

# Je mets le connector Mysql python : mysql+pymysql + connection MySql : user + base de données
engine = create_engine("mysql+pymysql://root@localhost/fromagerie")
# Ma requête SQL
sql_select_Query = "select * from dataw_fro where qte > 5 and timbrecli >0"

# df : DataFrame
df = pandas.read_sql(sql_select_Query, engine) # load comme un ficher CSV par exemple
print(df)

print(30*'*')

var=['cpcli', 'datcde', 'codcli']
df_copy=df[var].copy()
print(df_copy)

print(30*'*')

cpcli=df.groupby('cpcli').apply(lambda x: x)
print(cpcli)

print(30*'*')

datcde=df.groupby('datcde').apply(lambda x: x)
print(datcde)

print(30*'*')

codcli=df.groupby('codcli').apply(lambda x: x)
print(codcli)

print(30*'*')

prixmean=df['prixcond'].mean()
print(prixmean)

print(30*'*')
'''
prixmean2=df.groupby('prixcond').mean()
print(prixmean2)

print(30*'*')
'''
somme= df['qte'].sum()
print(somme)

print(30*'*')

df.plot(kind='bar', x='libobj', y='points')
plt.show()
df.plot(kind='pie', x='libobj', y='Nbcolis')
plt.show()