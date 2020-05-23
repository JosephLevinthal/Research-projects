# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0=float(input("escolha a velociade"))
angulo= float(input("escolha o angulo"))
d= float(input("escolha a distancia"))
a=radians(angulo)
g=9.8
r= (v0**2*sin(2*a))/g
if(  abs(d-r) < 0.1 ):
	m= "sim"
	print(m)
else:
	m= "nao"
	print(m)