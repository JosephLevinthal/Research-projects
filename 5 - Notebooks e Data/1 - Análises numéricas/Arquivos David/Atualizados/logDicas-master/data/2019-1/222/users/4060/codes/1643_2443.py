# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
raio=float(input("raio do tanque: "))
coluna=float(input("altura da coluna: "))
numero=int(input("numero desejado: "))
v_esfera=(4*pi*raio**3)/3
v_ar=(pi*coluna**2*(3*raio-coluna))/3
v_combustivel=v_esfera-v_ar
if(numero==1):
	print(round(v_ar, 4))
else:
	print(round(v_combustivel, 4))