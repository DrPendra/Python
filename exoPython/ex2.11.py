print("---Exo 2.11---")

from easygui import *

list=[0,1,2,3,4]
x=float(input())
for i in list:
    if float(i) == x:
        a=float(i)
        break
msgbox()