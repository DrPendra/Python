from random import random


class nombremagique:

    def __init__(self):
        self.nombreinconnu=round(random()*30)

    def getStart(self):
        print("J'ai choisi un nombre entre 1 et 30 inclus")
        print("A vous de le déviner en moins de 5 tentatives")
        tentative = 1
        while tentative < 6:
            if tentative == 1:
                print("premier essai")
            if tentative == 2:
                print("second essai")
            if tentative == 3:
                print("troisième essai")
            if tentative == 4:
                print("quatrième essai")
            if tentative == 5:
                print("dernier essai")
            print("Choisie ton nombre:")
            nbr = int(input())
            if nbr > self.nombreinconnu:
                print("c'est trop grand")
            elif nbr < self.nombreinconnu:
                print("c'est trop petit")
            else:
                print("Bravo, tu as gagné")
                break
            tentative += 1
            if tentative == 6:
                print("Tu as perdu! le nombre était", self.nombreinconnu)

j=nombremagique()
j.getStart()

