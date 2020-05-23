# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

a = float(input("Qual o tamanho do lado A?"))
b = float(input("Qual o tamanho do lado B?"))
c = float(input("Qual o tamanho do lado C?"))

k = a
l = b
m = c

f = k/2 + l/2 + m/2

F = (f - k)
G = (f - l)
H = (f - m)

D = f*F*G*H

from math import *

A = sqrt(D)

print(round(A, 5))
