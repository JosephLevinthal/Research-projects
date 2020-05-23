vida = float(input("Vida:\n"))
d1 = float(input("D1:\n"))
d2 = float(input("D2:\n"))
from math import*
dano = (sqrt(5*d1) + pi**(d2/3))
danosofrido = int(dano)
resultado = vida - danosofrido
print(resultado)