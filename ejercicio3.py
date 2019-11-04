# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:45:10 2019

@author: niko1
"""


def factorial(n,pos,cont):
    fact=cont
    if(pos<=n):
        fact=fact*pos
        fact=factorial(n,pos+1,fact)
        return fact
    return fact


valor=int(input("Escriba un valor: "))
print('el factorial de ',valor,' es ',factorial(valor,1,1))