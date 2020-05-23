from numpy import*
n = array(eval(input("Qtd. de glicose: ")))
i = 0 #posicao do vetor
g = 0 #ocorrencias
while (i < size(n)):
	if (n[i] > 99):
		g = g + 1
		print(i)
	else:
		g = g + 0
	i = i + 1
print(g)
	
		