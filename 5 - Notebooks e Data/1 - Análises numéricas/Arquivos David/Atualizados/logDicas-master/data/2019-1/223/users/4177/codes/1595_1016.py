# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
c=float(input("Valor de c: "))

s=(a+b+c)/2

A=s*(s-a)*(s-b)*(s-c)
R=(sqrt(A))
print(round(R,5))
