from numpy import *
notas = array(eval(input("Notas: ")))
alunos = array(eval(input("Alunos: ")))
i = 0
f = 0
a = 0
r = 0
soma = 0
while(i < size(notas)):
	if (notas[i] == -1):
		f = f + 1
	elif (notas[i] >= 6):
		a = a + 1
	else:
		(notas[i] < 6) and (notas != -1)
		r = r + 1
	if (notas[i] != -1):
		soma = soma + notas[i]
	if (notas[i] == max(notas)):
		maior = i
	i = i + 1


med = soma/(size(notas) - f)	
print(f)
print(a)
print(r)
print(round(med, 2))		
print(alunos[maior])
