from numpy import *

faltas = array(eval(input()))
v = zeros(6, dtype=float)

soma = 0
for x in range (size(faltas)):
	if(faltas[x] == 2):
		v[0]=v[0]+1
		soma=soma + 1
	elif(faltas[x] ==3):
		v[1] = v[1] + 1
		soma=soma + 1
	elif(faltas[x] == 4):
		v[2] = v[2] +1
		soma=soma + 1
	elif(faltas[x]==5):
		v[3] = v[3] +1
		soma=soma + 1
	elif(faltas[x]==6):
		v[4] = v[4] +1
		soma=soma + 1
	elif(faltas[x] == 7):
		v[5] = v[5] +1
		soma=soma + 1
soma = soma / 100
aux = 0
for x in range (size(v)):
	aux = round((v[x]/soma), 1)
	v[x] = aux
print(v)
