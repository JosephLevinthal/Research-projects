from math import*

a = int(input("life: "))
d1 = int(input("dado1: "))
d2 = int(input("dado2: "))

d = int(sqrt(5 * d1) + pi ** (d2 / 3))
r = a - d

print(r)


