#B.1.a.1.
import random
from math import *
liste=[]

for i in range(5):
    liste.append(i+4)

def moyenne(liste):
    sum=0
    for i in liste:
        sum +=i
    return sum/len(liste)

ave_tableau=moyenne(liste)
print(ave_tableau)

#B.1.a.2.

def occurence(liste):
    occ={}
    for i in liste:
        t=liste.count(i)
        dic={str(i): t}
        occ.update(dic)
    return occ

print(occurence([1,2,5,1,6,9,8,3,5,2,4,1,4]))


#B.1.a.3.
count=0
liste.append(10)
for i in liste:
    if i>=10:
        count +=1
print(count)

#B.1.a.4.
max=0
liste.append(6)
for i in liste:
    if i > max:
        max=i

print(max)


#B.1.a.4.
def estpresent(liste, nbr):
    for i in liste:
        if i == nbr:
            return True
    return False

print(estpresent(liste, 5))
print(estpresent(liste, 2))

#B.1.b.1.

def tableau(n):
    liste=[]
    for i in range(n) :
        liste.append(random.randint(0, 1000))
    return liste

print(tableau(18))

#B.1.b.2.

def tableauentiers(n):
    liste=[]
    for i in range(n) :
        liste.append(i)
    random.shuffle(liste)
    return liste

print(tableauentiers(18))

#B.1.b.3.
import time



tab=tableau(100)
ave=moyenne(tab)
present=estpresent(tab, 20)
print(ave, present)

