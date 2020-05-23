# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
raio = float(input("digite:  "))
altura = float(input("altura: "))
numero = int(input("qual volume: "))

from math import*

volumedaesfera = ((4*pi)*(raio**3))/3
volumedacalota = ((pi*altura**2)*(3*raio - altura))/3
diferenca = volumedaesfera - volumedacalota

if  (numero == 1):
	  print(round(volumedacalota, 4))
		
else:
	 print(round(diferenca, 4))