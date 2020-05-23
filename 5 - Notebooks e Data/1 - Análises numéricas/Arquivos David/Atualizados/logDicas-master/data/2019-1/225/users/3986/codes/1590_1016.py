# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
a=float(input("valor 1: "))
b=float(input("valor 2: "))
c=float(input("valor 3: "))
s=(a + b + c) / 2
A=sqrt(s * (s - a) * (s - b) * (s - c)) 
print(round(A,5))