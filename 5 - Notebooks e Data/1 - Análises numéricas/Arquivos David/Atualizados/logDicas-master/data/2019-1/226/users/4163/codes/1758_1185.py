from numpy import*
g = array(eval(input("insira o nivel de glicose")))
#acumuladoras
i = 0 #posicao do vetor 
n = 0 #numero de ocorrencias

while (i<size(g)):
	if(g[i]>99):
		n = n + 1
		i = i + 1
		print(i-1)
	else:
		i = i + 1
print(n)