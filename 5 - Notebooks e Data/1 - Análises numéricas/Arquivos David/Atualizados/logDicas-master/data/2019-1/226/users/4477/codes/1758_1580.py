# Modulo do Vetor
from numpy import *
# Vetor de entrada
notas = (array(eval(input("Determine as notas: "))))
nomes = (array(eval(input("Determine os nomes: "))))
# Variavel
i = 0
f = 0
a = 0
r = 0
soma = 0
maior = 0
# Laço
while (i<size(notas)):
	if (notas[i] == -1.0):
		f = f + 1
	elif (notas[i] >= 6.0):
		a = a + 1
	elif (notas[i] < 6.0) and (notas[i] != -1):
		r = r + 1
	if (notas[i] != -1):
		soma = soma + notas[i]	
	if (notas[i] == max(notas)):
		maior = i
	i = i + 1
# Saida
print(f)
print(a)
print(r)
print(round( soma/(size(notas) - f), 2))
print(nomes[maior])

