from math import floor
from random import random

def pendu():
    mots = ["python", "programme", "ordinateur", "algorithme", "langage", "variable", "boucle", "fonction", "objet", "condition"]
    randoms = floor(random()*10)
    choice=mots[randoms]
    liste=list()

    for i in range(len(choice)):
        liste.append("_")

    count = 0
    while True:
        print("".join(liste))
        print("Entrez une lettre ou '?' pour abandonner : ")
        lettre = input()

        if lettre == "?":
            break

        for i in range(len(choice)):
            if lettre == choice[i]:
                liste[i] = lettre

        count += 1

        if "".join(liste) == choice:
            print("Bravo ! Le mot ", choice, " a été trouvé en ", count, " coups")
            break




pendu()