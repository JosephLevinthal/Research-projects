from math import *
np=int(input("digite o numero de pessoas na sala: "))

result= (1-(factorial(365)/factorial(365-np) * 1/365**np))

result2= result*100
print(round(result2,2))
