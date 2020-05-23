# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
r = float(input("raio: "))

from math import *
area = pi * (r ** 2)
vol = 4 * pi * (r ** 3) / 3

print(round(area, 3))
print(round(vol, 3))