from numpy import*

vetor = array(eval(input("vetor de numeros interios")))
m = 1
for i in range(size(vetor)):
	m = m * vetor[i]
j = m**1/(size(vetor)+ 1)
print(round(j,2))