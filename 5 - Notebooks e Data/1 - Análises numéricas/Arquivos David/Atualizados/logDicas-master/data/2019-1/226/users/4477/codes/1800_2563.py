# Módulo
from numpy import *
# Entrada
v = array(eval(input("Vetor: ")))            # Médias Finais
# Laço de termino "While"
while (size(v) > 1):
	m = 0
	for i in v:
		if (i >= 5) and (i < 7):
			m = m + 1
	# Saída
	print(m)
	# Repetição
	v = array(eval(input("Vetor: ")))