import math

n = int(input("Numero de pessoas: "))

p = 1 - ((math.factorial(365))/(math.factorial(365 - n))) * (1/365**n)

print(round(p*100,2))

