# Leitura das entradas dos lados de um triangulo:
a = float(input("digite um numero para o lado a do triangulo: "))
b = float(input("digite um numero para o lado b do triangulo: "))
c = float(input("digite um numero para o lado c do triangulo: "))

# Calculo do semiperimetro:
s = (a + b + c)/2

# Calculo da area:
from math import sqrt
A = sqrt(s*(s - a)*(s - b)*(s - c))
print(round(A, 5))

