# Teste seu codigo aos poucos.
from math import*
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)/2


# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
print(round(sqrt(s*(s-a)*(s-b)*(s-c)), 5))