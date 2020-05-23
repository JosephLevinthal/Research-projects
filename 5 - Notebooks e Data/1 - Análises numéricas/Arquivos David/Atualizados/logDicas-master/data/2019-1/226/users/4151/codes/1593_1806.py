x=int(input("numero de pessoas: "))
from math import*
p=1-factorial(365)/factorial(365-x)*1/365**x
probabilidade = p*100
print(round(probabilidade,2))