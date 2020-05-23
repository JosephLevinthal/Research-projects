from math import*
n = int(input("a"))
r = 1-(factorial(365)/factorial(365-n))*(1/365**n)
print(round(r*100,2))

