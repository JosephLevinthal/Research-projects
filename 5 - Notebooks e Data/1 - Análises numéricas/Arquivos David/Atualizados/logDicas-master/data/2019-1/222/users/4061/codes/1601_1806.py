from math import *
n = int(input("digite pessoas"))
p = 1-((factorial(365)/factorial(365-n))*(1/(365**n)))
x = p*100
print(round(x, 2))