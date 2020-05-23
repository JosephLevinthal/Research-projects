vi = float(input("Vida inicial: "))

D1 = int(input("Numero sorteado no dado 1: "))
D2 = int(input("Numero sorteado no dado 2: "))

from math import*

dano = int((((sqrt(5*D1)) + (pi**(D2/3)))))

eq1 = (vi - dano)

print(eq1)