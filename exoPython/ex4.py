#1.
print("---Exo 4.1---")

liste=[17, 38, 10, 25, 72]
print(liste)
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.reverse()
print(liste)
print(liste.index(17))
liste.remove(38)
print(liste)
print(liste[2:3])
print(liste[:2])
print(liste[-1])
print(liste[3:])
print(liste[:])
print(liste[-1])

#2.
print("---Exo 4.2---")
import re

truc=[]
machin=[0.0,0.0,0.0,0.0,0.0]
print(truc, machin)
for i in range(4):
    print(i)
for i in range(4,8):
    print(i)
for i in range(2,10,2):
    print(i)
chose=[0,1,2,3,4,5]
print(chose.__contains__(3))
print(chose.__contains__(6))

#3.
print("---Exo 4.3---")

list=chose
print([x+3 for x in list])

#4.
print("---Exo 4.4---")
list=chose
print([ i+3 for i in list if i > 2])


#5.
print("---Exo 4.5---")

print([i + j for i in "abc" for j in "de"])

#6.
print("---Exo 4.6---")

print(sum([i for i in range(10)]))

#7.
print("---Exo 4.7---")

X=set('abcd')
Y=set('sbd')

print(X, Y)
print(X.__contains__('c'))
print(Y.__contains__('a'))
print(X-Y)
print(Y-X)
print(X.union(Y))
print(X.intersection(Y))

#8.
print("---Exo 4.8---")

def compterMot(a):
    dic={}

print(compterMot("je me présente, je m'appelle Henri"))


#9.
print("---Exo 4.9---")

dico={"Au":{"Te/Tf" : [2970, 1063], "Z/A":[79, 196.967]},
         "Ga":{"Te/Tf" : [2237, 29.8], "Z/A":[31, 69.72]}}

print(dico["Au"]["Z/A"][0])

#10.
print("---Exo 4.10---")


#11.
print("---Exo 4.11---")

