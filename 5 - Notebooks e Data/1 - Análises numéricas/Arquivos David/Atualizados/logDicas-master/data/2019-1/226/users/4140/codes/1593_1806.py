from math import *
n=int(input());
resultado= 1- ((factorial(365))/factorial(365-n))*(1/365**n);
resultado2=resultado*100
print(round(resultado2,2));