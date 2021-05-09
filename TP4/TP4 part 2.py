
import math
from math import *
import matplotlib.pyplot as mp

# Question 1

# méthode du point fixe

def PointFixe(g,x0,epsilon,Nitermax):

    x = x0
    n = 0
    e = epsilon
    l_n = []
    l_xn = []
    l_en = []

    while n != Nitermax and abs(g(x)-x)>= e:

        n = n + 1
        x = g(x)
        l_n.append(n)
        l_xn.append(x)
        l_en.append(abs(g(x)-x)) # évolution des erreurs commises: xn-alpha
        print(g(x))
        print("nombre d'itérations", n)
        print("écart", abs(g(x)-x)) 

    return l_n, l_xn, l_en



# méthode de Newton

def Newton(f,fder,x0,epsilon,Nitermax):

    xold = x0
    # xnew = xold - f(xold)/fder(xold)
    n = 0
    l_n = []
    l_xn = []
    l_en = []
    while abs(xold-(xold - f(xold)/fder(xold)))>epsilon and n!=Nitermax:

        n = n+1
        xnew = xold - f(xold)/fder(xold)
        xold = xnew
        l_n.append(n)
        l_xn.append(xold)
        l_en.append(abs(xold - xnew))

    return l_n, l_xn, l_en

# méthode de la dichotomie

def Dichotomie(f,a0,b0,epsilon,Nitermax):

    an=a0
    bn=b0
    e=epsilon
    n=0
    l_n = []
    l_an = []
    l_en = []

    while abs(bn-an) > e and n < Nitermax:

        m=(an+bn)/2
        if f(an)*f(m)<=0:
            bn=m
        else:
            an=m
        n+=1        
        l_n.append(n)
        l_an.append(an)
        l_en.append(abs(bn - an))

    return l_n, l_an, l_en


# méthode de la sécante

def Secante(f,x0,x1,epsilon,Nitermax):

    e = epsilon
    n = 0
    l_n = []
    l_xn = []
    l_en = []

    while abs(x1-x0)>e and n<Nitermax:

        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        n+=1
        l_n.append(n)
        l_xn.append(x1)
        l_en.append(abs(x1 - x0))

    return l_n, l_xn, l_en

# Question 2

def fpointfixe(x):
    return x**4+3*x-9

def fdichotomie(x):
    return x**4+3*x-9

def fnewton(x):
    return x**4+3*x-9
def fnewtonder(x):  #dérivée fnewton
    return 4*(x**3)+3

def fsecante(x):
    return x**4+3*x-9

# Question 2

PointFixe =  PointFixe(fpointfixe,1,10**(-15),100)
Dichotomie = Dichotomie(fdichotomie,0,2,10**(-15),100)
Newton = Newton(fnewton,fnewtonder,1,10**(-15),100)
Secante = Secante(fsecante,1,2,10**(-15),100)

# affichage graphique des résultats 

lx = Dichotomie[0]
ly = [abs(i - Dichotomie[1][-1]) for i in Dichotomie[1]]
mp.plot(lx, ly, 'b', label='Dichotomie')
    
lx = Newton[0]
ly = [abs(i - Newton[1][-1]) for i in Newton[1]]
mp.plot(lx, ly, 'g', label='Newton')
    
lx = Secante[0]
ly = [abs(i - Secante[1][-1]) for i in Secante[1]]
mp.plot(lx, ly, 'r', label='Secante')
    
lx = PointFixe[0]
ly = [abs(i - PointFixe[1][-1]) for i in PointFixe[1]]
mp.plot(lx, ly, 'y', label='PointFixe')
    
mp.semilogy()
mp.legend()
mp.grid()
mp.show()