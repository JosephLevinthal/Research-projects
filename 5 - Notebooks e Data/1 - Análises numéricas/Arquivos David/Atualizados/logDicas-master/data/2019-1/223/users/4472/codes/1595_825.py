# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

import math

raio = input("Digite o raio: ")
r = float(raio)

A = math.pi * (r ** 2)
V = (4/3) * math.pi * (r ** 3)

print (round((A), 3))
print (round((V), 3))

