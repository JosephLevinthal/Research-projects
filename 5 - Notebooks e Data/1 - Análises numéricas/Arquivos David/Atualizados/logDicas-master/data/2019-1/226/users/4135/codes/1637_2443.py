# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("Digite o raio do tanque:"))
x = float(input("Digite a altura na parte superior do tanque:"))
num = int(input("Digite a opcao desejada? (1/2) "))
V1 = (pi*(x**2)*(3*r-x))/3
V2 = ((4*pi*(r**3))/3)-V1
if (num == 1):
	print(round(V1,4))
else:
	print(round(V2,4))