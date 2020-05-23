# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("a"))
b=float(input("b"))
c=float(input("c"))
s=a/2+b/2+c/2
from math import *
area=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))