#1.
import math

print("---Exo 2.1---")

print("Donnez moi un nombre pour que j'en fasse sa racine")
inconnu= float(input())
if inconnu > 0 or inconnu == 0:
    print("la racine de", inconnu, "est", inconnu**(1/2))
else:
    print("ce nombre est négatif, il me sera impossible de trouver sa racine")

#2.
print("---Exo 2.2---")

print("Donnez moi 2 mot à classer")
mot1=input()
mot2=input()
if mot1 > mot2:
    print("le mot", mot2,"se situe avant le mot", mot1)
elif mot1 == mot2:
    print("nous avons, là, le même mot")
else:
    print("le mot", mot1, "se situe avant le mot", mot2)

print("Donnez moi 2 mots et je les comparerai")
mot1=input()
mot2=input()
long1=len(mot1)
long2=len(mot2)
if long1 > long2:
    print("le mot", mot1, "est plus long que le mot", mot2)
elif long1 == long2:
    print("nous avons, là, la même longueur de mot")
else:
    print("le mot", mot2, "est plus long que le mot", mot1)

print("Donnez moi 2 mots et je les comparerai")
mot1=input()
mot2=input()
long1=len(mot1)
long2=len(mot2)
res=long1 >= long2
if res:
    print("le mot", mot1, "est plus long que le mot", mot2)
else:
    print("le mot", mot2, "est plus long que le mot", mot1)


#3.
print("---Exo 2.3---")

pSeuil = 2.3
vSeuil = 7.41
pression=float(input())
volume=float(input())
if pression > pSeuil and volume > vSeuil:
    print("Arret immédiat")
elif pression > pSeuil:
    print("augmenter le volume")
elif volume > vSeuil:
    print("diminuer le volume")
else:
    print("tout va bien")

#4.
print("---Exo 2.4---")

a=0
b=10

while a<b:
    print(a)
    a=a+1

while b!=0:
    if b%2 != 0:
        print(b)
    b=b-1

#5.
print("---Exo 2.5---")

for i in range(0,11,1):
    print(i)

#6.
print("---Exo 2.6---")

mot=input()
for i in mot:
    print(i)

#7.
print("---Exo 2.7---")

for i in range(0,15,3):
    print(i)

#8.
print("---Exo 2.8---")

for i in range(0,11,1):
    print(i)
    if i==5:
        break

#9.
print("---Exo 2.9---")

for i in range(0,11,1):
    if i!=5:
        print(i)

#10.
print("---Exo 2.10---")

for i in range(-3, 4, 1):
    try:
        print(math.sin(i)/i)
    except ZeroDivisionError:
        print("on ne peut diviser par 0")


