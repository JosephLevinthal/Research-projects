from numpy import*
from numpy.linalg import*

matriz = array(eval(input("dia da semana:")))

dia = zeros((7), dtype=int)

for j in range(size(dia)):
	dia[j] = sum(matriz[:,j])
	#print(dia)
x = 0
for i in range(size(dia)):
	if(dia[i] >= max((dia))):
		x = i + 1
		print(x)