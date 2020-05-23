# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("o raio do tanque: "))
x= float(input("a altura da coluna de ar: "))
n = input(" o numero da opcao desejada (1/2): ")

v1 = (4 * pi * (r**3))/3

v2 = (pi*(x**2)* ((3*r)-x))/3

if(n== "1"):
	print(round(v2, 4))
else:
	print(round(v1-v2, 4))