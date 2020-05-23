from math import*
pv = int(input("Digite pontos de vida: "))
D1 = int(input("Digite valor 1: "))
D2 = int(input("Digite valor 2: "))
d = int(sqrt(5*D1) + pi**(D2/3))
f = pv - d
print(f)