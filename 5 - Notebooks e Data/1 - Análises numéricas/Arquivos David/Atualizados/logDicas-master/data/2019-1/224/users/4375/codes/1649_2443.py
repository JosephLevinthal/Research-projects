# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
raio=float(input("raio"))
altura=float(input("altura"))
num=int(input("num"))
from math import*
vol=((4*pi)*(raio**3))/3
volar=(pi*(altura**2)*(3*raio-altura))/3
volcomb=vol-volar
if(num==1):
	print(round(volar,4))
else:
	print(round(volcomb,4))
