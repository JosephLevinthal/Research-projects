# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float (input(''))
b = float(input(''))
c = float(input(''))
from math import sqrt
s = (a + b + c) / 2
A = sqrt (s*(s - a)*(s - b)*(s - c))
print (round(A, 5))