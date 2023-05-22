from ponyentity import *

@db_session
def createFournisseur():
    Fournisseur(nom="bob billy",
                adresse="1 rue de la bonne santé", ville="Tarascon",
                codepostal="13150")
    Fournisseur(nom="lama bernard",
                adresse="33 rue de la prison", ville="Saint-Symphorien",
                codepostal="33113")
    Fournisseur(nom="Culaid Roland",
                adresse="69 rue de l'amour", ville="Tarascon",
                codepostal="13150")
@db_session
def print_all_fournisseur():
    # pass
    select(f for f in Fournisseur).show()

if __name__ == '__main__':
    # createFournisseur()
    print_all_fournisseur()