# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import* 

r = float(input("raio: "))
h = float(input("altura: "))
num = int(input("opcao desejada 1 ou 2: "))

v1 = 4*pi*(r**3)/3
v2 = (pi*(h**2)*(3*r - h))/3

if (num == 2):
	a = v1-v2
	print(round(a ,4))
else:
	print(round(v2, 4))
	
