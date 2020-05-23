import math
from math import pi 

hp = int(input("initialhp: "))
D1 = int(input("valor dado1: "))
D2 = int(input("valor dado2: "))

dano = ((5*D1)**0.5)+pi**(D2/3)

finalhp = (hp - int(dano))

print(finalhp)

