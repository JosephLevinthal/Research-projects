# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

v=float(input("velocidade inicial:"))
a=radians(float(input("angulo do vetor:")))
D=abs(float(input("distancia entre passaro e porco:")))
g=9.8

R=(v)**2*sin(2*a)/g
p=abs(D-R)
if(p<0.1):
	mensagem="sim"
else:
	mensagem="nao"
print(mensagem)