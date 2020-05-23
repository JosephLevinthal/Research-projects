from math import *
HP = int(input("vida inicial: "))
D1 = int(input("dado um: "))
D2 = int(input("dado dois: "))

exp = D2/3
base = 5*D1
dano = (base**0.5) + (pi**exp)
remain = HP - int(dano)

print(int(remain))