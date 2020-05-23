# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("Raio do tanque: "))
h = float(input("Altura da coluna: "))
n = int(input("calculo de (1/2): "))
volume_calota = pi * h**2 * (3*r - h) / 3
volume_esfera = 4*pi*r**3 / 3
if (n == 1):
	msg = volume_calota
else:
	msg = volume_esfera - volume_calota
print(round(msg, 4))
	



			 

			 
			 
			 
