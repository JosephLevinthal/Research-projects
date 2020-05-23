# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("Raio do tanque: "))
a = float(input("Altura da coluna de ar: "))
o = float(input("Opcao desejada: "))
c = (pi*(a**2)*(3*r-a))/3
if (o == 1):
	v = c
else:
	v = (4*pi*(r**3))/3 - c
print(round(v,4))	
	