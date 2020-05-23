# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
raio = float(input("insira o raio:"))
from math import pi

A= pi * raio**2
V= 4/3 * pi * raio**3
print(round(A, 3))
print(round(V, 3))


