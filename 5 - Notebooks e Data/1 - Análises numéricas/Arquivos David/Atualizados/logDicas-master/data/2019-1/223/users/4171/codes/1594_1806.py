from math import*
n = (int(input("numero de pessoas: ")))
a = (365 - n)
y = 1 - (factorial(365))/(factorial(a)) * (1/365**n)
b = y*100
print(round(b,2))

