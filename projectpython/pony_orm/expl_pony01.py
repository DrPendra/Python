from pony.orm import *

# 1
db = Database()
# 2
db.bind(provider='mysql', host='localhost', user='root', passwd='', db='biblio')

# 3
class T_client(db.Entity):
    codcli = PrimaryKey(int, auto=True)
    genrecli = Optional(str)
    nomcli = Optional(str)
    prenomcli = Optional(str)

# 4
db.generate_mapping(create_tables=True)

# 5
with db_session:
    c1 = T_client(genrecli="Mme", nomcli="CGE", prenomcli="CGE 01")
    commit()
    print(c1.nomcli,c1.codcli)
    select(c for c in T_client if c.codcli > 41200)[:10].show()

