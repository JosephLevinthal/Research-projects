from numpy import*
vet = array(eval(input("glicose: ")))

i = 0
cont = 0

while(i < size(vet)):
	if(vet[i] > 99):
		print(i)
		cont = cont + 1
	i = i + 1

	
print(cont)
	