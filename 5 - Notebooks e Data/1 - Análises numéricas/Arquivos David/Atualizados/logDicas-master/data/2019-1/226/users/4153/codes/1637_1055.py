# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
vo = float(input("Insira a velocidade inicial: "))    #velocidade inicial
a = float(input("Insira o angulo: "))                 #angulo do vetor de lancamento
D = float(input("Insira a distancia horizontal: "))   #distancia horizontal
g = 9.8                                               #aceleracao da gravidade

A = radians(a)                                        #convercao para radianos
S = sin(2*A)                                          #calculo do seno
R = ((vo**2)*S)/g                                     #formula

tol = abs(D - R)                                      #tolerancia


if(tol < 0.1):
	msg = "sim"
else:
	msg = "nao"
print(msg)