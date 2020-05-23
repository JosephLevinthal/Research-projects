# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("lado um: "))
b = float(input("lado dois: "))
c = float(input("lado tres: "))
from math import *
s = (a+b+c) / 2
area = sqrt(s*(s - a)*(s - b)*(s - c))
print(round(area, 5))