def someDiv(nbr):
    somme=0
    for i in range(nbr-1,0,-1):
        if nbr % i == 0:
            somme= somme +i
    return somme

def estParfait(nbr):
    somme=someDiv(nbr)
    return nbr*2==somme+nbr


def estPremier(nbr):
    list=[]
    for i in range(nbr - 1, 1, -1):
        if nbr % i == 0:
            list.append(i)
    return len(list) == 0

def estChanceux(nbr):
    list = []
    for i in range(0, nbr-1, 1):
        if estPremier(i*i+i+nbr) == False:
            list.append(i)
    return len(list) == 0




if __name__ == '__main__':
    print(someDiv(18))

    print(estPremier(17))
    print(estPremier(18))

    print(estParfait(6))
    print(estParfait(15))

    print(estChanceux(17))
    print(estChanceux(18))

    print(someDiv(12))
    print(estParfait(6))
    print(estPremier(31))
    print(estChanceux(11))

