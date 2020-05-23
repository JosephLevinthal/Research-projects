# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
a = float(input("Lado1: "))
b = float(input("Lado2: "))
c = float(input("Lado3: "))
s = (a + b +c) / 2
a1 = sqrt(s*((s - a) * (s - b) * (s - c)))
print(round(a1, 5))
