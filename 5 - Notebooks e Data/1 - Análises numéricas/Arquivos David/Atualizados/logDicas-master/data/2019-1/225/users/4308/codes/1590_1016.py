# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a = float(input("a"))
b = float(input("b"))
c = float(input("c"))
s = ( a + b + c) / 2
Area = sqrt(s * (s - a) * (s - b) * (s - c))
print(round(Area,5))