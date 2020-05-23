from math import*
V = int(input("Vidas iniciais: "))
D1 = int(input("D1: "))
D2 = int(input("D2: "))

D3 = int(sqrt(5 * D1) + pi ** (D2/3))
total = V - D3

print(int(total))