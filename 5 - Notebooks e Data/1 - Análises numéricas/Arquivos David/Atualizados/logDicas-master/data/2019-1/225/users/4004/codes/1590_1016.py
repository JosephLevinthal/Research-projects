# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import *

a = float(input("number "))
b = float(input("number "))
c = float(input("number "))

S = a + b + c
s = S/2
t = (s - a)*(s - b)*(s - c)*s
A = sqrt(t)

print(round(A, 5))