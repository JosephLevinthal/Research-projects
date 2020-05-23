import math as m
n = int(input("numero do Grupo: "))

P = 1 - ((m.factorial(365)/m.factorial(365-n))*(1/(365**n)))
Pn = P*100
print(round(Pn, 2))