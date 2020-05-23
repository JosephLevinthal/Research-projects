# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo
from math import *
A = float(input("Digite a:"))
B = float(input("Digite b:"))
C = float(input("Digite c:"))
S = ((A + B + C)*1/2)
AR = sqrt(S*((S-A)*(S-B)*(S-C)))
print (round (AR,5))