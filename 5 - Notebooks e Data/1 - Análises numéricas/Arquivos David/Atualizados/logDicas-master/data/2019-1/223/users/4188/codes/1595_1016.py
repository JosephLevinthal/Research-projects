# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("digite o valor do a: "))
b=float(input("digite o valor de b: "))
c=float(input("digite o valor do c: "))
s=(a+b+c)/2
from math import sqrt
a=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(a,5))