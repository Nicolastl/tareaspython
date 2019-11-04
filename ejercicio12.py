# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:31:45 2019

@author: niko1
"""

def resolver1(pal1,pal2):
    #frozenset re ordena los caracteres en formato ASCII, pasando, por ejemplo, la palabra cosa a a-c-o-s
    x = frozenset(pal1)
    y = frozenset(pal2)
    if(x==y):
        print(pal2,' es un anagrama de ',pal1)
    else:
        print(pal2,' no es un anagrama de ',pal1)

def resolver2(pal1,pal2):
    #este metodo vera si las letras de ambas palabras coinciden, si todas coinciden, quiere decir que son anagramas, pues elimina la revision de una misma letra
    aux = []
    aux2 = []
    pasa=1
    for i in range (len(pal1)): #vamos letra por letra evaluando la palabra 1
        for j in range (len(pal1)): #lo mismo con la palabra 2
            if(pal1[i]==pal2[j]):
                if not aux:
                    aux.append(j)
                    aux2.append(pal2[j])
                    break
                else:
                    pasa=1
                    for k in range (len(aux)):
                        if(aux[k]==j):
                            pasa=0
                    if(pasa==1):
                        aux.append(j)
                        aux2.append(pal2[j])
    if(len(pal1)==len(aux2)):
        print(pal2,' es un anagrama de ',pal1)
    else:
        print(pal2,' no es un anagrama de ',pal1)
def resolver3(x,y):
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
            print(y,' no es un anagrama de ',x)
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
                    print(contx[i])
                    if(contx[i]!=conty[j]):
                        print(y,' no es un anagrama de ',x)
                        seguir=0
                        break
    if(seguir==1):
        print (y,'es un anagrama de ',x)

                
                

x=input('escriba una palabra: ')
y=input('escriba otra palabra: ')
if(len(x)==len(y)): #len() nos da el tamaño del string, si son iguales, entrara en alguna funcion
    resolver1(x,y)
    resolver2(x,y)
    resolver3(x,y)
else:
    print(y,'no puede ser un anagrama de ',x,' pues no tienen el mismo largo de letras')

