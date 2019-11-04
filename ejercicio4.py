# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:06:53 2019

@author: niko1
"""
import math
def modulo(x,y):
    mod=x*x+y*y
    return (math.sqrt(mod))
def angulo(x,y):
    ang=y/x
    return (math.degrees(math.atan(ang)))
x=int(input("Escriba un valor para X: "))
y=int(input("Escriba un valor para Y: "))
print ('el modulo es: ',modulo(x,y), 'y el angulo es: ',angulo(x,y))