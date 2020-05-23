# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import sqrt
a = float(input("insira o lado do triangulo: "))
b = float(input("insira o lado do triangulo: "))
c = float(input("insira o lado do triangulo: "))

s = (a+b+c)/2
s1 = (s - a)
s2 = (s - b)
s3 = (s - c)

A = float(sqrt(s * s1 * s2 * s3))

print(round(A , 5))
