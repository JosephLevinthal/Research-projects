# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
v1 = float(input("a:"))
v2 = float(input("b:"))
v3 = float(input("c:"))
s = (v1+v2+v3)/2
from math import*
A = sqrt(s*(s-v1)*(s-v2)*(s-v3))
print(round(A,5))