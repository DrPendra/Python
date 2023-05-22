#E.1.2
import random
import time
import pygnuplot.gnuplot


tab=[]
[tab.append(random.randint(0,20)) for i in range(21)]

def copie(t):
    t2=[]
    for i in t:
        t2.append(i)
    return t2

tab2=copie(tab)
tab2[5]=100

print(tab)
print(tab2)

def inverse(t):
    t2 = []
    for i in range(len(t)-1, -1,-1):
        t2.append(t[i])
    return t2

tab3=inverse(tab)
tab3[5]=100

print(tab)
print(tab3)

def tableau_premiers_entiers(n):
    t=[]
    for i in range(n+1):
        t.append(i)
    return t

def tableau_premier_entiers_melanges(n):
    t=tableau_premiers_entiers(n)
    random.shuffle(t)
    return t

def tableau_premier_entiers_inverses(n):
    t=tableau_premiers_entiers(n)
    t=inverse(t)
    return t

print(tableau_premiers_entiers(10))
print(tableau_premier_entiers_inverses(10))
print(tableau_premier_entiers_melanges(10))

def ligne_dans_fichier(f, n, t):
    file = open(f, 'w')
    file.write('{}  {}\n'.format(n, t))

ligne_dans_fichier('test.dat', 1, 5)

def tri_a_bulle(t):
    for j in range(1, len(t)):
        for i in range(1, len(t)):
            if t[i-1] > t[i]:
                tmp=t[i-1]
                t[i-1]=t[i]
                t[i]=tmp
    return t

def temps_tri_bulle(t):
    t1=time.perf_counter()
    tab=tri_a_bulle(t)
    t2=time.perf_counter()
    return t2-t1

j=tableau_premier_entiers_melanges(10)
temps=temps_tri_bulle(j)
print(temps, "seconde")

def stats_melange(nmin, nmax,pas, fois):
    t = []
    for i in range(nmin, nmax + 1, pas):
        t.append(i)
    for i in range(fois):
        random.shuffle(t)
        temps=temps_tri_bulle(t)
        ligne_dans_fichier('tri_a_bulle.dat', i, temps)

def stats_ordonne(nmin, nmax,pas, fois):
    t = []
    for i in range(nmin, nmax + 1, pas):
        t.append(i)
    for i in range(fois):
        temps=temps_tri_bulle(t)
        ligne_dans_fichier('tri_a_bulle_ordonne.dat', i, temps)

def stats_inverse(nmin, nmax,pas, fois):
    t = []
    for i in range(nmax, nmin - 1, pas):
        t.append(i)
    for i in range(fois):
        temps=temps_tri_bulle(t)
        ligne_dans_fichier('tri_a_bulle_inverse.dat', i, temps)

stats_melange(100,1000,100,5)
#pygnuplot.gnuplot.plot_data('tri_a_bulle.dat')

def index_minimum(t, d, f):
    min=t[f]
    indmin=f
    for i in range(d, f+1):
        if t[i] < min:
            min=t[i]
            indmin=i
    return indmin

def insertion(e,t,n):
    i=0
    while t[i]<e:
        i+=1
    t1=t[:i]
    t2=[e]
    t3=t[i:n]
    return t1+t2+t3

def tri_extraction(t):
    for i in range(len(t)-1):
        n=index_minimum(t, i, len(t)-1)
        y=t[i]
        t[i]=t[n]
        t[n]=y
    return t

def tri_insertion(t):
    n=len(t)
    for i in range(n-1):
        t1 = t[:i]
        t2 = t[i]
        t3 = t[i+1:len(t)]
        t4=t1+t3
        t4=insertion(t2, t4, n-1)
    return t4

'''
def tri_rapide(t):
    if len(t)==1:
        return t
    else:
        petit=[]
        grand=[]
        for i in range(len(t)):
            if t[i] <= t[len(t)-1]:
                petit.append(t[i])
            if t[i] > t[len(t)-1]:
                grand.append(t[i])
        return tri_rapide(petit)+[t[n]]+tri_rapide(grand)

print(tri_rapide(j))
'''