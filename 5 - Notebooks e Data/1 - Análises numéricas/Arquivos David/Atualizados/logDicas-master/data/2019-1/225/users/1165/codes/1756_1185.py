from numpy import*
v = array(eval(input("Informe os valores do vetor: \n")))
i = 0
soma = 0

while(i<size(v)):
	if(v[i]>99):
		print(i)
		soma = soma + 1
	i = i + 1
print(soma)