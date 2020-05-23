# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
raio=float(input("digite o raio:"))
altura=float(input("digite a altura:"))
numero=float(input("digite onumero:"))
from math import*
volume1= (4*pi)*(raio**3)/3
volume2= (pi*(altura**2)*(3*raio-altura))/3
valordocomb= volume1-volume2
if(numero==1):
	print(round(volume2,4))
else:
	print(round(valordocomb,4))
