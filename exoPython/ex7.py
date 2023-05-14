#1.
print("---Exo 7.1---")

class MaClasse:
    x = 23
    y = x + 5

    def affichage(self):
        z = 42
        print( self.y, z)

M=MaClasse
M.affichage(M)

#2.
print("---Exo 7.2---")

class Vecteur2D:

    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def affichage(self):
        print([self.x, self.y])

    def ajoutvecteur(self, x, y):
        return Vecteur2D(self.x + x, self.y + y)

V0=Vecteur2D()
V1=Vecteur2D(2,3)

print(V0.x, V0.y)
print(V1.x, V1.y)

#.3
print("---Exo 7.3---")

V2 = Vecteur2D(-2, 3)
V1.affichage()
V2.affichage()
V1.ajoutvecteur(V2.x, V2.y).affichage()
