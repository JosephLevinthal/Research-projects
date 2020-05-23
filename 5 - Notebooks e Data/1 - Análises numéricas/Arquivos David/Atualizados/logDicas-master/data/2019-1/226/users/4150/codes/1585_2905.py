# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu 

from math import*

a = float(input("valor a: "))
b = float(input("valor b: "))
c = float(input("valor c: "))

s = (a + b + c)/2

area = (sqrt(s*(s-a)*(s-b)*(s-c)))

print(round(area, 5))
