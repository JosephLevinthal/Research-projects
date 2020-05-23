# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
g1 = float(input("Digite lado 1: "))
g2 = float(input("Digite lado 2: "))
g3 = float(input("Digite lado 3: "))

s = (g1 + g2 + g3) / 2

from math import*

A = sqrt(s* (s-g1) * (s-g2) * (s-g3))
print(round(A,5))