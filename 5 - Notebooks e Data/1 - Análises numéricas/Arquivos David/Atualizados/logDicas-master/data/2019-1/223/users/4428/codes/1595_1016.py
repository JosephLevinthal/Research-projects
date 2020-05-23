# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

s = (a+b+c)/2

area = s*(s-a)*(s-b)*(s-c)
from math import*
sqrt(area)


print(round(sqrt(area), 5))