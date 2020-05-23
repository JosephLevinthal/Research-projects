from numpy import *
notas = array(eval(input()))
peso = 1
i = 0
calculo = 0
soma = 0
while(i<size(notas)):
	calculo = (notas[i]*peso) + calculo
	soma = soma + peso
	peso = peso + 1
	i = i + 1

print(round(calculo/soma,2))