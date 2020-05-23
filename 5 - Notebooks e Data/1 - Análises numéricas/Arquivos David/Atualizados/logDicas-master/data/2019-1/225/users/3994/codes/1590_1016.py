# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
A = float(input())
B = float(input())
C = float(input())

p=(A+B+C)/2
G= float(sqrt(p*(p-A)*(p-B)*(p-C)))
print(round(G,5))



