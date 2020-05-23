from numpy import *
notas = array(eval(input("Notas: ")))
i = 0

while(notas[i] != min(notas)):
	i = i + 1
	
soma = sum(notas) - notas[i]	
med = soma/(size(notas) - 1)

print(round(med, 2))