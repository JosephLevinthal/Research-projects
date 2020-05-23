# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("Digite raio: "))
x = float(input("Digite altura: "))
opcao = int(input("1 ou 2?: "))
J = (pi * (x**2) *(3*r - x))/3 # volume de ar
A = (4 * pi * (r**3))/3 # volume total
if(opcao == 1):
	print(round(J,4))
else:
	V = A - J

	print(round(V,4))