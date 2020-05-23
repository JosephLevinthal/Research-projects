# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("raio: "))
x = float(input("altura: "))
opcao = float(input("opcao:"))
if (opcao == 1):
	print((pi*x**2) * (3*r - x ) / 3)
else:
	print((4*pi*r**3) / 3 -  (pi*x**2) * (3*r - x ) / 3)
	

					 
