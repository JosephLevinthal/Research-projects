# Modulo
from numpy import *
# Entradas
v = array(eval(input("Vetor: ")))
# Variaveis
i = 0
n = 0
# Laço
while (i<size(v)):
	if (v[i] >= 0):
		n = n + 1
	i = i + 1
	
tam_final = size(v) - n
vet_final = zeros(tam_final, dtype=int)
# Variavel_2
i = 0
j = 0
# Laço_2
while (i<size(v)):
	if (v[i]>=0):
		vet_final[j] = v[i]
		j = j + 1
	i = i + 1
# Saida
print(vet_final)