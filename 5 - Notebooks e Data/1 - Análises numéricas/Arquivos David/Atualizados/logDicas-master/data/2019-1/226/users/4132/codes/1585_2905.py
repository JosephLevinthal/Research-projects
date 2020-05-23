# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
	
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
area=sqrt(area)

print(round(area,5))
