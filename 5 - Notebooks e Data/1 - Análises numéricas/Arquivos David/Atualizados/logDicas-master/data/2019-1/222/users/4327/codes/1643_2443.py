# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
from math import*
r=float(input("raio: "))
alt=float(input("altura: "))
num=int(input("indique 1 para  vol. do ar ou 2 para o vol. de combustivel"))

vr=(4*pi*r*r*r)/3

vcal=((pi*alt*alt)*(3*r-alt))/3

vcom=vr-vcal

if(num==1):
 	print(round(vcal,4))
else:
	print(round(vcom,4))