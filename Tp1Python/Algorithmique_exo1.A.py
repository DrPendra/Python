#Algorithmique exo1 1.
print("---exo A.1---")

a="une chiane de caractère"
b=5

print("il y a", len(a), "caractères \nainsi que la variable est:", b)

# le \n permet de passer à la ligne si on venez à l'enlever,
# il n'aura pas de retour à la ligne

#Algorithmique exo1 2.
print("---exo A.2---")

count=0
while count<101:
    print(count)
    count += 1

for i in range(101):
    print(i)

from turtle import *

color('black', 'white')
begin_fill()
i=0
while i != 4:
    forward(200)
    left(90)
    i+=1
left(180)
i=0
while i !=3:
    forward(200)
    right(120)
    i+=1

def carre(l):
    begin_fill()
    i=0
    while i != 4:
        forward(l)
        left(90)
        i += 1

def triangle(l):
    begin_fill()
    i = 0
    while i != 3:
        forward(l)
        right(120)
        i += 1
left(90)
forward(100)
carre(200)
triangle(200)

#Algorithmique exo1 3.
print("---exo A.3---")

A = []
B = [0,1,2,3,4,5,6,7,8,9]
print("la longueur de la liste A est", len(A))
print("la longueur de la liste B est", len(B))
B[5]=50.1
print(B)
B.remove(B[6])
print(B)
B.append("bonjour")
B.append([188, "Ah une autre liste"])
print(B)
for i in B:
    print(i)
    print(type(i))


#Algorithmique exo1 4.
print("---exo A.4---")
import random

print(random.randint(0,20))
#randint prend un entier aléatoire entre 0 et 20
print(random.randrange(0, 10))
#randrange vide prendra un nombre aléatoire entre 0 et 1
print(random.choice(B))
#choice permet de retourner un élément aléatoire de la liste founis
random.shuffle(B)
print(B)
#shuffle permet de mélanger les éléments au sein d'une liste de manière aléatoire



