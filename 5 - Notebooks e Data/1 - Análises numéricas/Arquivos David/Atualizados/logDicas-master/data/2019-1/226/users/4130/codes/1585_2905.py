# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
l1 = float(input("lado 1: "))
l2 = float(input("lado 2: "))
l3 = float(input("lado 3: "))

semip = (l1 + l2 + l3) / 2

from math import sqrt

area = sqrt(semip * (semip - l1) * (semip - l2) * (semip - l3))

print(round(area, 5))