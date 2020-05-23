# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
# primeiro lado do triangulo
a = float(input("digite um numero:"))
# segundo lado do triangulo
b = float(input("digite um numero:"))
# terceiro lado do triangulo
c = float(input("digite um numero:"))
u = (a+b+c)/2
from math import *
area = sqrt(u*(u-a)*(u-b)*(u-c))
print(round(area, 5))