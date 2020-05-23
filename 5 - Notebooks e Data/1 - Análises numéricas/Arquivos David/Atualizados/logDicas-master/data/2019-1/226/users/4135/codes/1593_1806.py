n = float(input("Digite o numero de pessoas:"))
from math import *
p_n= (1 - (factorial(365)/factorial(365-n))*(1/(365**n)))
print (round(p_n*100,2))
