# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("valor do lado A:"))
b=float(input("valor do lado B:"))
c=float(input("valor do lado C:"))
s=float((a+b+c)/2)
from math import*
A=float(sqrt(((s-a)*(s-b)*(s-c))*s))

print(round(A,5))