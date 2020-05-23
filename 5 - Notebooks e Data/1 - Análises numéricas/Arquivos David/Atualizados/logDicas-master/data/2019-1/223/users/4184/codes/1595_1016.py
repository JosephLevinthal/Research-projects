# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*

a=float(input("insira o valor de a:"))
b=float(input("insira o valor de b:"))
c=float(input("insira o valor de c:"))

s=(a+b+c)/2

a=s*(s-a)*(s-b)*(s-c)
r=(sqrt(a))
print(round(r,5))