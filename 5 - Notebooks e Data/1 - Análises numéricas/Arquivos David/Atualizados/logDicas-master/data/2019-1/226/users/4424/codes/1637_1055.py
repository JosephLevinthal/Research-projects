# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("Digite um numero: "))
a=float(input("Digite um numero: "))
d=float(input("Digite um numero: "))
a=(radians(a))
r=(((v0)**2)*sin(2*a))/9.8
d=abs(r-d)
if(d<0.1):
	print("sim")
else:
	print("nao")

print()