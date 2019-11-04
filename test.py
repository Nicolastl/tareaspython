# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:06:03 2019

@author: niko1
"""
x='aaea'
y='aaea'
cont=0
letrasx = []
letrasy = []
contx = []
conty = []
seguir=1
for i in range (len(x)):
    entra=1
    if not letrasx:
        letrasx.append(x[i])
        cont=cont+1
    else:
        for j in range (len(letrasx)):
            if(letrasx[j]==x[i]):
                entra=0
        if(entra==1):
            letrasx.append(x[i])
            cont=cont+1
cont=0
for i in range (len(y)):
    entra=1
    if not letrasy:
        letrasy.append(y[i])
        cont=cont+1
    else:
        for j in range (len(letrasy)):
            if(letrasy[j]==y[i]):
                entra=0
        if(entra==1):
            letrasy.append(y[i])
            cont=cont+1
for i in range (len(letrasx)):
    igual=0
    for j in range (len(letrasy)):
        if(letrasx[i]==letrasy[j]):
            igual=1
    if(igual==0):
        print(x,'no es un anagrama de ',y)
        seguir=0
        break
if(seguir==1):
    for i in range (len(letrasx)):
        contador=0
        for j in range (len(x)):
            if(letrasx[i]==x[j]):
                contador=contador+1
        contx.append(contador)
    for i in range (len(letrasy)):
        contador=0
        for j in range (len(y)):
            if(letrasy[i]==y[j]):
                contador=contador+1
        conty.append(contador)
for i in range (len(letrasx)):
    for j in range (len(letrasy)):
        if(letrasx[i]==letrasy[j]):
            if(contx[i]!=conty[j]):
                print(x,'no es un anagrama de ',y)
                seguir=0
                break
if(seguir==1):
    print (x,'es un anagrama de ',y)