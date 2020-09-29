# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:38:35 2020

@author: Slayer20
"""

import csv

exp=[]
imp=[]
with open("C:\Users\Slayer20\Downloads\Course Resources\synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        exp.append(linea[2])
        imp.append(linea[3])

imp.pop(0)
exp.pop(0)        
agrup = zip(exp,imp)

i=1
cont=[]
com=[]
while i <= len(agrup):
    o = agrup[i]
    x = agrup.count(o)
    com.append(o)
    cont.append(x)
    i=i+1
cont_com = zip(com,cont)    


mj = sorted(set(cont_com))
mj = set(cont_com)

def take_second(elem):
    return elem[1]

sorted(list(mj),key=take_second,reverse=True)



#2

import csv

transp=[]
valor=[]
with open("C:\Users\Slayer20\Downloads\Course Resources\synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        transp.append(linea[7])
        valor.append(linea[9])

transp.pop(0)
valor.pop(0)

transp_valor=dict(zip(transp,valor))        
print(transp_valor)

pais_valor =zip(transp,valor)

i=0
suma_paises=[]
pais_2 =[]
x= 0
y = 0
while i < len(pais_valor):
    if pais_valor[i][1] == pais_valor[i+1][1]:
        x = int(pais_valor[i][1]) + x
        y = pais_valor[i][0]
        suma_paises.append(x)
        pais_2.append(y)
        i=i+1
    else:
        x=0
        y=0
        i=i+i
    
final = zip(pais_2,suma_paises)   

print(list(final)) 


mj = sorted(set(full))
mj = set(full)



sorted(list(mj),key=take_second,reverse=True)

#3
import csv

pais=[]
valor=[]
with open("C:\Users\Slayer20\Downloads\Course Resources\synergy_logistics_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector: 
        pais.append(linea[2])
        valor.append(linea[9])

pais.pop(0)
valor.pop(0)

pais_valor=zip(pais,valor)        
pais_valor.sort()


i=0
suma_paises=[]
pais_2 =[]
x= 0
y = 0
while i < len(pais_valor):
    if pais_valor[i][1] == pais_valor[i+1][1]:
        x = int(pais_valor[i][1]) + x
        y = pais_valor[i][0]
        suma_paises.append(x)
        pais_2.append(y)
        i=i+1
    else:
        x=0
        y=0
        i=i+i
    
final = zip(pais_2,suma_paises)   

print(list(final))


final_v2 = dict(zip(pais_2,suma_paises))
print(final_v2)
sel=[]
x = 0
i=1
while i <= len(final_v2)+1:
    if final_v2[i][0] == final_v2[i+1][0]:
        i=i+1
        continue
    else:
        x = final_v2[i]
        sel.append(x)
        i= i+1
    
print(sel)    
    
    
mj = sorted(set(final))
mj = set(final)
print(final_v2)


sorted(list(mj),key=take_second,reverse=True)



