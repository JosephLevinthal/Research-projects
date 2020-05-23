from math import*

hp_i = int(input())
d1 = int(input())
d2 = int(input())

p1 = sqrt(5 * d1)
p2 = pi**(d2/3)
dano = p1 + p2
hp_f = hp_i - int(dano)

print(hp_f)