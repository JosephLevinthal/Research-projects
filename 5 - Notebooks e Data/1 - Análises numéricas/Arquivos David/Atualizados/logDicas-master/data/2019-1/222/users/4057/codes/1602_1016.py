# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
# primeiro lado do triangulo.
a = float(input("digite umnumero: "))
# segundo lado do triangulo.
b = float(input("digite umnumero: "))
# terceiro lado do triangulo.
c = float(input("digite umnumero: "))
s = (a+b+c)/2
from math import *
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area, 5))