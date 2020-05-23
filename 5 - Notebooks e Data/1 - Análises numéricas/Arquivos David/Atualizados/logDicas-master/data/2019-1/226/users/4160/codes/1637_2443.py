# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input("Digite o raio do tanque: "))
x = float(input("Digite a altura da coluna de ar (x) na parte superior do tanque: "))
n = int(input("Digite a opcao (1 ou 2): "))
from math import *
#esfera do raio r TOTAL:
v1 = (4 * pi * r ** 3) / 3
#calota esferica de raio r e altura x:
v2 = (pi * x**2 *(3*r - x))/ 3

if (n == 1):
	resp = v2
	print(round(resp,4))
else: 
	resp = v1 - v2
	print(round(resp,4))
	
	