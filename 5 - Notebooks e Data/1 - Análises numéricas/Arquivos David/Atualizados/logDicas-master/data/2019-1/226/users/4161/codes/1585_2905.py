# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
l1 = float(input("valor de L1: "))
l2 = float(input("valor de L2: "))
l3 = float(input("valor de L3: "))
s = (l1 + l2 + l3)/2
area = sqrt(s*(s-l1)*(s-l2)*(s-l3))
print(round(area, 5))
