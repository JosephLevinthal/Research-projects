# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r=float(input("Digite o raio(R):"))
x=float(input("Digite a altura(X):"))
opcao=int(input("Digite a opcao(1/2):"))
var=(pi*(x**2)*(3*r-x)/3)
vesf=(4*pi*r**3/3)
vcomb=(vesf-var)
if(opcao==1):
	print(round(var,4))
if(opcao==2):
	print(round(vcomb,4))
	