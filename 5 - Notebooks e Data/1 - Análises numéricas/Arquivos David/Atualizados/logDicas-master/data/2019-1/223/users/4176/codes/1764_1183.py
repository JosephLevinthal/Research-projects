from numpy import* 

vet = array(eval(input("Vetor: ")))

posi = 0
tamanho = size(vet)
NPosit = 0
while(posi < tamanho):
	if(vet[posi] > 0):
		NPosit =  NPosit + 1
	posi = posi + 1
nvet = zeros(NPosit, dtype=int)
i = 0
i2 = 0
while(i < size(vet)):
	if(vet[i] > 0):
		nvet[i2] = vet[i]
		i2 = i2 + 1
	i = i+ 1
print(nvet)