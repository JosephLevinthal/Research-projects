# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

lado1 = float(input("digite o valor do lado"))
lado2 = float(input("digite o valor do lado"))
lado3 = float(input("digite o valor do lado"))
from math import *
s = (lado1 + lado2 + lado3)/2
A = sqrt(s*(s - lado1)*(s - lado2)*(s - lado3))

print(round(A, 5))