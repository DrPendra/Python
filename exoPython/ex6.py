#1.
print("---Exo 6.1---")

def fracine(a, b, c):
    delta= b*b-4*a*c
    r=[]
    if delta > 0:
        nb=2
        r.append((-b-delta)/2*a)
        r.append((-b+delta)/2*a)
    elif delta < 0:
        nb=0
    else:
        nb=1
        r.append(-b/2*a)
    res=(nb, r)
    return res

print(fracine(1,-3,2))
print(fracine(1,-2,1))
print(fracine(1,-1,1))

#2.
print("---Exo 6.2---")

