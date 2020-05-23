# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = float(input("digite o lado A "))
b = float(input("digite o lado B "))
c = float(input("digite o lado C "))
from math import *
s = (a + b + c)/2
Area = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(Area, 5))