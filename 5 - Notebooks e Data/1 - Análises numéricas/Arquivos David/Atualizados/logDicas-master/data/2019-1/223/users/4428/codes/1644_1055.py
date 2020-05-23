# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*
v0 = float(input("Velocidade Inicial: "))
a = radians(float(input("Angulo do Vetor: ")))
D = float(input("Distancia do passaro para o porco: "))
g = 9.8

R = (((v0**2)*sin(2*a))/g)

if(abs(R-D) <= 0.1):
	mensagem = "sim"
else: 
	mensagem = "nao"

print(mensagem)

