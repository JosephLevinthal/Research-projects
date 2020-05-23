from math import*

n = float(input('digite n: '))

P = round(((1 - ( factorial(365) / factorial(365 - n) )*(365**(-n)))*100),2)
print(P)
