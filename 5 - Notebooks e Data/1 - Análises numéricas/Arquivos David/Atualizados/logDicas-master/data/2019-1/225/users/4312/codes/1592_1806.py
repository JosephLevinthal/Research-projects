n = float(input("Informe um numero qualquer:\n"))
from math import*
p = (1 - (factorial(365)/factorial(365-n)) * (1/(365**n)))*100
print(round(p,2))