import math
from math import cos,sin,exp,log,tan


# méthode de la dichotomie 

def Dichotomie(f,a0,b0,epsilon,Nitermax):

    e = epsilon
    a = a0
    b = b0
    n = 0

    while abs(b-a) > e and n< Nitermax:

        m = (a+b)/2
        if (f(a)*f(m))<=0:
            b = m
        else:
            a = m
        n = n+1

    return m,n

#méthode de la sécante

def secante(f, x0, x1,e):

    n=1

    while abs(x1-x0) > e:

        n = n+1
        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        x0,  x1  = x1,  x2
        
    return x1,n


# Définir les fonctions à étudier 
def f1(x):
    return x**4+3*x-9

def f2(x):
    return x-3*cos(x)+2

def f3(x):
    return x*exp(x)-7


#affichage des fonctions méthode de la dichotomie 
print ('méthode de la dichotomie')

print('f1')
print(Dichotomie(f1,-3,-1,1e-10,5e4))
print('f2')
print(Dichotomie(f2,0,2,1e-10,5e4))
print('f3')
print(Dichotomie(f3,0,2,1e-10,5e4))


#affichage des fonctions méthode de la sécante
print ('méthode de la sécante')

print('f1')
print(secante(f1,-2,-1,1e-10))
print('f2')
print(secante(f2,-4,-3,1e-10))
print('f3')
print(secante(f3,1,2,1e-10))