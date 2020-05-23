# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("Raio:"))
a = float(input("Altura:"))
n = int(input("Opcao desejada:"))
v1 = ((4*pi*(r)**3))/3
v2 = ((pi*(a)**2)*((3*r)-a))/3
eq = (v1 - v2)
if (n == 1):
	print(round(v2,4))
else:
	print(round(eq,4))