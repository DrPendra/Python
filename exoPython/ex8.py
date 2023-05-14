#1.
print("---Exo 8.1---")

class Rectangle:

    def __init__(self, long=0, larg=0):
        self.rectangle = [long, larg]

    def affichage(self):
        print(self.rectangle)

    def surface(self):
        return self.rectangle[0]*self.rectangle[1]


class Carre(Rectangle):

    def __init__(self, long):
        self.carre= [long]*2

    def affichage(self):
        print(self.carre)

    def surface(self):
        return self.carre[0]*self.carre[1]


R=Rectangle(4,5)
C=Carre(5)
R.affichage()
C.affichage()
print(R.surface())
print(C.surface())

#1.
print("---Exo 8.2---")