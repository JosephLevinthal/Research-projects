from math import *
n=int(input("numero de pessoas: "))
print(float(round(((1-(factorial(365)/factorial(365-n))*(1/(365**n)))*100),2)))