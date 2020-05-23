import math

a = float(input("lado 1 do triangulo: "))
b = float(input("lado 2 do triangulo: "))
c = float(input("lado 3 do triangulo: "))

s = (a + b + c) / 2

A = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(round(A, 5))