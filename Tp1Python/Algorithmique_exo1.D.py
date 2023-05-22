#D.1.1
import random
import math

def index_minimum(t, d, f):
    min=t[f]
    indmin=f
    for i in range(d, f+1):
        if t[i] < min:
            min=t[i]
            indmin=i
    return indmin

def tri_a_bulle(t):
    for j in range(1, len(t)):
        for i in range(1, len(t)):
            if t[i-1] > t[i]:
                tmp=t[i-1]
                t[i-1]=t[i]
                t[i]=tmp
    return t


#D.1.2
def recherche(t, e):
    i=0
    while i < len(t):
        if t[i] == e:
            ind=i
            return ind
        i +=1

def dichotomie(t, e):
    if t[0]==e:
        return 0
    elif t[len(t)-1]==e:
        return len(t)-1
    else:
        a=0
        b=len(t)-1
        i=math.floor((len(t)-1)/2)
    while t[i]!=e and a!=b-1 :
        if e > t[i]:
            a=i
            i=math.floor((b+a)/2)
        if e < t[i]:
            b=i
            i=math.floor((b+a) / 2)
    if e ==t[i]:
        return i
    else:
        return None

def insertion(e,t,n):
    i=0
    while t[i]<e:
        i+=1
    t1=t[:i]
    t2=[e]
    t3=t[i:n]
    return t1+t2+t3

#D.1.3

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

if __name__ == "__main__":

    tab=[]
    [tab.append(random.randint(0,20)) for i in range(21)]

    print(tab)
    print(index_minimum(tab, 4, 15))

    tob=tri_a_bulle(tab)
    print(tob)

    print(recherche(tob, 10))
    print(dichotomie(tob, 10))

    print(insertion(10, tob, len(tob)))

    print(tri_extraction(tab))
    print(tri_insertion(tab))
