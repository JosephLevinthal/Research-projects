# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
rt = float(input("Raio do tanque:"))
h = float(input("Altura da coluna de ar:"))
n = int(input("Opcao 1: VOLUME DE AR. Opacao 2: VOLUME DE COMBUSTIVEL."))

ve = (4*pi*(rt**3))/3
vce = (pi*(h**2) * (3*rt - h))/3

if (n == 1):
	x = vce
else:
	x = ve - vce
	
print(round(x, 4)	)