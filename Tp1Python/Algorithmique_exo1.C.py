import random


def promotion(listedetudiant, nombrededisciple):
    promo=[["nom"]]
    for i in range(nombrededisciple):
        promo.append(["discipline"+str(i+1)])
    for i in range(len(listedetudiant)):
        promo[0].append(listedetudiant[i])
        for j in range(len(promo)-1):
            promo[j+1].append(0)
    return promo

promo=promotion(["billy", "bob", "archibald"], 3)
print(promo)

for i in range(1, len(promo)):
    for j in range(1, len(promo[0])):
        promo[i][j]=random.randint(0,20)
print(promo)
def moyenneetudiant(promo, etudiant):
    indice = promo[0].index(etudiant)
    somme=0
    for i in range(1,len(promo)):
        somme+=promo[i][indice]
    moy=somme/(len(promo)-1)
    return moy

print(moyenneetudiant(promo, "billy"))

def moyennedispline(promo, discipline):
    for i in range(len(promo)):
        if discipline == promo[i][0]:
            indice=i
    somme=0
    for i in range(1,len(promo[0])):
        somme+=promo[indice][i]
    moy=somme/(len(promo)-1)
    return moy

print(moyennedispline(promo, "discipline1"))

def maxetudiant(promo):
    liste=[]
    for i in range(1,len(promo[0])):
        liste.append(moyenneetudiant(promo, promo[0][i]))
    max=0
    for i in liste:
        if i >max:
            max=i
    ind= liste.index(max)
    etudiant= promo[0][ind+1]
    return etudiant, max

def minetudiant(promo):
    liste = []
    for i in range(1, len(promo[0])):
        liste.append(moyenneetudiant(promo, promo[0][i]))
    min = 20
    for i in liste:
        if i < min:
            min = i
    ind = liste.index(min)
    etudiant = promo[0][ind + 1]
    return etudiant, min

print(maxetudiant(promo))
print(minetudiant(promo))

