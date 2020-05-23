# Módulo
from numpy import *
# Entrada
MF = array(eval(input("Media Final: ")))           # Média Final	
PA = array(eval(input("Presenca: ")))              # Presença
CH = array(eval(input("Carga horaria: ")))         # Carga Horária
# Contador do Vetor
cont = zeros(3, dtype=int)
# Laço "For"
for i in range(size(MF)):
	if (MF[i] >= 5) and (PA[i] >= (0.75 * CH)):
		cont[0] = cont[0] + 1
	elif (MF[i] < 5):
		cont[1] = cont[1] + 1
	elif (PA[i] < (0.75 * CH)):
		cont[2] = cont[2] + 1
# Saída
print(cont)