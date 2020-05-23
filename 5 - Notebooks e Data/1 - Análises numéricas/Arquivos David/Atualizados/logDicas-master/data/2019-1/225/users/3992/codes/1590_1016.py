# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a = float(input("lado 1: "))
b = float(input("lado 2: "))
c = float(input("lado 3: "))

s = (a+b+c)/2
x = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(x,5))