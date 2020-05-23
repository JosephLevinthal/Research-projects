# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
x = float(input("comprimento do lado a: "))
y = float(input("comprimento do lado b: "))
z = float(input("comprimento do lado c: "))
s = (x+y+z)/2
a = sqrt(s*(s-x)*(s-y)*(s-z))
print(round(a, 5))