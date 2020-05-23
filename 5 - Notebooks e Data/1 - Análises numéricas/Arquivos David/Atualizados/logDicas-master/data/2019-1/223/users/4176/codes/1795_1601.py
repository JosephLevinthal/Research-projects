from numpy import*

vet = array(eval(input("Digite o tempo: ")))

i= 0
posi = 0

while (i < size(vet)):
	if(vet[posi] < vet[i]):
		posi += 1
	i += 1

else:
	print(i)
