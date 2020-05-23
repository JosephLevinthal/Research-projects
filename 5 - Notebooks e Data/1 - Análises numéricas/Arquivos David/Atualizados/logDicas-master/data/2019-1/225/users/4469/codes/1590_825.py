import math

r = float(input("Entre com o raio: "))

a = math.pi * (r ** 2)

v = (4 / 3) * math.pi * (r ** 3)

print(round(a, 3))
print(round(v, 3))