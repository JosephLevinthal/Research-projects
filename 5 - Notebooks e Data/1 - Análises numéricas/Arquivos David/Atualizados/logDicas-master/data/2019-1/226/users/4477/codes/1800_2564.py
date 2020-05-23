# Módulo
from numpy import * 
# Entradas
TA = array(eval(input("Gols do time A: ")))
TB = array(eval(input("Gols do time B: ")))
# Contador do vetor
cont = zeros(3, dtype=int)
# Laço "For"
for i in range(size(TA)):
	if (TA[i] > TB[i]):
		cont[0] = cont[0] + 1
	elif (TA[i] == TB[i]):
		cont[1] = cont[1] + 1
	elif (TA[i] < TB[i]):
		cont[2] = cont[2] + 1
# Saída
print(cont)