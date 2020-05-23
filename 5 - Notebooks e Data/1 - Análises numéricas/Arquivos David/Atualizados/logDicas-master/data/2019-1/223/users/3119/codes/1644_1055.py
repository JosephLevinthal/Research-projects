# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

#Entradas
v = float(input("Qual a velocidade inicial? "))
a = radians(float(input("Qual o angulo? ")))
d = float(input("Distancia entres os dois: "))

g = 9.8

R = ((v**2) * sin(2*a))/g

if(abs(R - d) <= 0.1):
	mensagem = "sim"
else:
	mensagem = "nao"
print(mensagem)	