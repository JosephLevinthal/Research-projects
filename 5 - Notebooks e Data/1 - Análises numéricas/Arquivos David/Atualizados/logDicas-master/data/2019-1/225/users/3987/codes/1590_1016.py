# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("o comprimento do lado a do triangulo e:"))
b = float(input("o comprimento do lado b do triangulo e:"))
c = float(input("o comprimento do lado c do triangulo e:"))
s = ((a+b+c)/2)
from math import *
sqrt(s)
A = sqrt(s*((s-a)*(s-b)*(s-c)))
print(round(A,5))