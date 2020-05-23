# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r=float(input("raio do tanque:"))
x=float(input("altura:"))
opcao=input()
vol_esf=((4*pi*(r**3))/3)
calota=((pi*(x**2)*(r*3-x))/3)
if(opcao=="1"):
	v= calota
else:
	v=vol_esf -calota
print(round(v,4))