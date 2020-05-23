# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*

r = float(input("Qual o raio? "))
h = float(input("Qual a altura da coluna? "))
x = int(input("1/2"))

v1 = (4*math.pi*r**3)/ 3
v2 = ((math.pi*(h**2) * (3*r - h))/ 3

if(x == 1):
	print(round(v2, 4))
else:
	print(round(v2 - v1, 4))