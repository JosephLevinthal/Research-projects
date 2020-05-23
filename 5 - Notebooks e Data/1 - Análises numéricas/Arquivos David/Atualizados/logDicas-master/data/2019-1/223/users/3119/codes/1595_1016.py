# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import*

a = float(input("Digite o comprimento a: "))
b = float(input("Digite o comprimento b: "))
c = float(input("Digite o comprimento c: "))

s = (a+b+c)/2

area = sqrt(s*(s-a)*(s-b)*(s-c))

print(round(area, 5))