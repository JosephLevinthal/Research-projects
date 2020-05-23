from math import *
#Entrada dos dados:
k = int(input("Digite um numero natural maior do que zero: "))

x=1 #apenas termo da serie, se k for =1, o laco nao eh executado
soma = 1 # soma do primeiro termo = 1
while(x < k): #condicao do laco, numero de termos eh inferior ao numero pedido pelo usuario
	fac = 1/factorial(x) #calculo das parcelas adicionais, i. e., do segundo termo em diante
	soma = soma + fac #acrescimo do segundo termo em diante
	x = x+1 #incremento no numero de termos
print(round(soma, 8))