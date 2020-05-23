# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

r = float(input("Valor do raio:"))
alt = float(input("Valor da altura:"))
opcao = float(input("Volume de ar (1) Volume do combustivel (2):"))

v_esfera = (4 * pi * r**3)/3
v_calota = ((pi * alt**2) * (3*r - alt))/3


if(opcao == 2):
	print(round(v_esfera - v_calota,4))
else:
	print(round(v_))