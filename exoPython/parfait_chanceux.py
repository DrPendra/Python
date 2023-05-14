import parfait_chanceux_m as pcm
from easygui import msgbox

chanceux=[]
parfait=[]

#réduit à 100 car cela met trop de temps jusqu'à 1000
for i in range(2, 201, 1):
    if pcm.estParfait(i):
        parfait.append(i)
    if pcm.estChanceux(i):
        chanceux.append(i)

msgbox("les chanceux sont : "+str(chanceux)+" et les parfaits sont : "+str(parfait), "resultat", "OK")