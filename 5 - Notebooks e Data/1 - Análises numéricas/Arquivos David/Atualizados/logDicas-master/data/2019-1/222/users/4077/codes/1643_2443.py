# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
from math import *
raio = float(input("raio do tanque: "))
x = float(input("altura do ar: "))

opcao = int(input("volume do ar (1) ou do combustivel (2)? "))
calota = pi/3 * x**2 * (3 * raio - x)
if (opcao == 1):
	volume = calota
else:
	volume = 4/3 * pi * raio**3 - calota
print(round(volume, 4))
	


