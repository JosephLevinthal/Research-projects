from numpy import*

vet = array(eval(input("Digite o vetor: ")))
d1 = 1
media = sum(vet) / len(vet)

for i in range(size(vet)):
	p = abs(vet[i]-media)
	d1 = d1 * p

s = (d1)**(1/size(vet))

print(round(s,3))
	