# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
g=9.8
Vo=float(input("Vo: "))
alpha=radians(float(input("alpha:")))
D=float(input("D:"))
R=((Vo)**2*sin(2*alpha))/g
if(abs(D-R)<=0.1):
	print("sim")
else:
	print("nao")


