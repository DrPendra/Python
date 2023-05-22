from ponyconfig import *

class Fournisseur(db.Entity):
    id = PrimaryKey(int, auto=True)
    nom= Required(str)
    adresse= Required(str)
    ville = Required(str)
    codepostal= Required(str)
    tel = Optional(str)


db.generate_mapping(create_tables=True)