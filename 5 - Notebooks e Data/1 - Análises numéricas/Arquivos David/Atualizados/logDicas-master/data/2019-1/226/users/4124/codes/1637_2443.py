# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("Raio do tanque: "))
x = float(input("Altura da coluna de ar: "))
opc = int(input("Opcao desejada (1 = volume de ar, 2 = volume de combustivel): "))
if(opc == 2):
	v = (4 * pi * r**3) / 3 - (pi *(x**2)*(3*r - x)) / 3
else:
	v = (pi *(x**2)*(3*r - x)) / 3
print(round(v, 4))