from math import floor
from random import random

class Pendu(list):

    def __init__(self, listes):
        mots = listes
        randoms = floor(random() * 10)
        self.choice = mots[randoms]
        self.liste = list()

        for i in range(len(self.choice)):
            self.liste.append("_")



    def getstart(self):
        count = 0
        while True:
            print("".join(self.liste))
            print("Entrez une lettre ou '?' pour abandonner : ")
            lettre = input()

            if lettre == "?":
                break

            for i in range(len(self.choice)):
                if lettre == self.choice[i]:
                    self.liste[i] = lettre

            count += 1

            if "".join(self.liste) == self.choice:
                print("Bravo ! Le mot ", self.choice, " a été trouvé en ", count, " coups")
                break



j=Pendu(["python", "programme", "ordinateur", "algorithme", "langage", "variable", "boucle", "fonction", "objet",
                "condition"])
j.getstart()