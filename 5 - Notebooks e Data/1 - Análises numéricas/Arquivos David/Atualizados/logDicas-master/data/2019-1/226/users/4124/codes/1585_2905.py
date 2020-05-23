# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *
a = float(input("Comprimento do lado a: "))
b = float(input("Comprimento do lado b: "))
c = float(input("Comprimento do lado c: "))

s = ((a + b + c) / 2)

area = (sqrt(s * (s - a) * (s - b) * (s - c))) 
print(round(area, 5))
