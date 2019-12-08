# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:51:16 2019

@author: niko1
"""

def obtenerH(a,b,n):
    h=(b-a)/n                               #para obtener el valor de h, necesario en este metodo
    return h
def obtenerNodos(a,h,contador):
    f=a+h*contador
    return f
def obtenerResultado(f,n,h):
    resultado=0
    aux=0
    for i in range(len(f)):
        if(i==0 or i==len(f)-1):
            aux=f[i]**2                     #en este caso, usaremos como integral x al cuadrado, en python **2 representa elevar al cuadrado
        else:
            aux=2*(f[i]**2)
        resultado+=aux
    resultado*=h/2
    return resultado
a=int(input("Escriba un valor para a: "))   #para resolver una integral de este tipo, debe ser una integral definida,esos valores serán los que corresponden a "a" y "b"
b=int(input("Escriba un valor para b: "))
n=int(input("Escriba un valor para n: "))   #para este tipo de integral, se repartirá en distintos valores, "n" entre más grande, más cercano será el valor resultante al real
h = obtenerH(a,b,n)
f = []
for i in range (n+1):
    f.append(obtenerNodos(a,h,i))
print ("el valor de la integral es: ",obtenerResultado(f,n,h) )