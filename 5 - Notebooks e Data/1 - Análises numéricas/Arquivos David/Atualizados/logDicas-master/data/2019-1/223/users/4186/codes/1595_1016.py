# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input('Insira o valor de A:'))
b=float(input('Insira o valor de B:'))
c=float(input('Insira o valor de C:'))

s=(a+b+c)/2

A=s*(s-a)*(s-b)*(s-c)
R=(sqrt(A))
print(round(R,5))