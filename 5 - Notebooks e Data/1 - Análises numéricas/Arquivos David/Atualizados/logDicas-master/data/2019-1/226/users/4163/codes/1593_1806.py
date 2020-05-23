from math import *
n= int(input("numero de pessoas"))
pn= 1-(factorial(365) / factorial (365 - n))*(1/365**n)
print(round(pn*100 ,2))