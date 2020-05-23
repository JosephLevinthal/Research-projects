# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import * 
r = float(input("Qual o raio do tanque? "))
x = float(input("Qual a altura da coluna de ar? "))
n = int(input("escolha: 1 indica o calculo do volume de ar e 2 indica o calculo do volume de combustivel no tanque. "))
if n == 1 : 
	V = ((pi * (x**2)) * ((3*r)- x))/3
	print(round(V, 4))
else : 
	V = ((pi * (x**2)) * ((3*r)- x))/3
	V1 = (4*pi*(r**3))/3
	d = V1 - V
	print(round(d, 4))