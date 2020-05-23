import math

hp = float(input("Pontos de vida iniciais: "))
d1 = int(input("D1: "))
d2 = int(input("D2: "))
dano = int(math.sqrt(5*d1) + math.pi**(d2/3))

print(round(hp-dano))