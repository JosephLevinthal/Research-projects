from numpy import *

vetor = array(eval(input("Valores: ")))

i = 0
n = size(vetor)
soma = 0

while i < size(vetor):
	soma = (vetor[i] ** 5) + 1
	#media = ((vetor[i] ** 5) + (size(vetor) - 1) ** 5 / size(vetor)
	soma = soma + 1
	
	soma2 = (size(vetor) - 1) ** 5
	m = soma2 / n
	media = m ** 0.2
	
	i = i + 1

print (round(media,2))
