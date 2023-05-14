#1
print("---Exo 3.1---")

def ftable(base, deb, fin, inc):
    list=[]
    for i in range(deb, fin+inc, inc):
        list.append(i*base)
    return list

print(ftable(15,0,15,1))

#2
print("---Exo 3.2---")
import math

def fcube(x):
    y=x*x*x
    return y

print(fcube(3))

def fvolumesphere(r):
    y=4/3*math.pi*fcube(r)
    return y

print("{0:.2f}".format(fvolumesphere(5)))

#3
print("---Exo 3.3---")
from easygui import integerbox

def maFonction(fonction, bornein, bornesup, nbPas):
    if bornein > bornesup:
        print("houston, nous avons un problème. la borne inférieur ne peux pas être supérieur de la borne supérieur")
        return 0
    list=[]
    for i in range(bornein, bornesup+nbPas, nbPas):
        f=fonction
        f=f.replace('x', str(i))
        value=eval(f)
        list.append(value)
    return list

fonction='2*3+x-5'
print(maFonction(fonction, 1, 5, 2))

#4
print("---Exo 3.4---")

def fvolMasseEllipsoide(a, b, c, MasseVol):
    vol= 4/3*math.pi*a*b*c
    Masse= MasseVol * vol
    tu=(vol, Masse)
    return tu

print(fvolMasseEllipsoide(2, 3, 4, 5))
print(fvolMasseEllipsoide(3, 6, 6, 10))
print(fvolMasseEllipsoide(4, 9, 8, 15))
print(fvolMasseEllipsoide(5, 12, 10, 20))

#5
print("---Exo 3.5---")

def fsomme(tuple):
    som=0
    for i in tuple:
        som= som + i
    return som

t1=(1,2,3,4,5,6,7,8,9)
print(fsomme(t1))

#6
print("---Exo 3.6---")

def fsomme2(tuple):
    a, b, c= tuple
    som = a+b+c
    print(som)

t2=(1,2,3)
fsomme2(t2)

#7
print("---Exo 3.7---")

def unDictionnaire(dictionnaire):
    for i,j in dictionnaire.items():
        print(i, j)

dic= { "pays":"Egypte", "capital":"Le Caire"}
unDictionnaire(dic)