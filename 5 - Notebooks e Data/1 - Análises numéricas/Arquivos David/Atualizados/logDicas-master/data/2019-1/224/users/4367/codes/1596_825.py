# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
r= float(input("escolha um valor para o raio"))
from math import*
A= pi*r**2
V= 4/3*pi*r**3
print(round(A, 3))
print(round(V, 3))