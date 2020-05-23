# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
lado1=float(input("lado 1: "))
lado2=float(input("lado 2: "))
lado3=float(input("lado 3: "))
s=(lado1+lado2+lado3)/2
from math import sqrt
A=sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
print(round(A,5))