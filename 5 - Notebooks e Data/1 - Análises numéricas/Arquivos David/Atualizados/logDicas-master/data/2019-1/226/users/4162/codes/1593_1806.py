n=int(input("insira a quantidade de pessoas: "))
from math import *
a= factorial(365)
b= factorial(365-n)
p=1-(a/b)*(1/(365**n))
pn=p*100
print (round(pn,2))

