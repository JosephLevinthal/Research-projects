p=int(input("pontoa de vida inicial: "))
d1=int(input("numero sortiado 1: "))
d2=int(input("numero sortiado 2: "))
from math import*
dano=int(sqrt(5*d1)+(pi**(d2/3)))
print(p-dano)