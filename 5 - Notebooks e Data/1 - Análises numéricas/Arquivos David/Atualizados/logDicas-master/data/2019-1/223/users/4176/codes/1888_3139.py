from numpy import*

vet = array(eval(input("Digite o Vetor: ")))

n = size(vet)
exp = 1/3

for i in vet:
	v= sum(vet[:-1])
	
m = ((sum(vet[:-1])**1/3)/n)**3

print(round(m, 2))