# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
from math import*
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = (a + b + c) / 2
a = sqrt(s*(s - a) * (s - b) * (s - c))
print(round(a, 5))