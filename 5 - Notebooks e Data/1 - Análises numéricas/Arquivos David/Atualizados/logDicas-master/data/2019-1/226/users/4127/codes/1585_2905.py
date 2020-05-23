# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*
l1=float(input("lado1: "))
l2=float(input("lado2: "))
l3=float(input("lado3: "))
sm= ((l1+l2+l3)/2)
area=(sqrt((sm*(sm-l1)*(sm-l2)*(sm-l3))))
print(round(area,5))