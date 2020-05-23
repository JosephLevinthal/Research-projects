from numpy import*

vet = array(eval(input(" ")))
g2 = 0
for i in range(size(vet)):
	if (vet[i] % 2 != 0):
		g2 = g2 + 1
vetor = zeros(g2, dtype=int)
cont = 0
for i in range(size(vet)):
	if(vet[i] % 2 != 0):
		vetor[cont] = vet[i]
		cont = cont + 1
print(vetor)
