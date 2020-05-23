from numpy import *
z = array(eval(input("Digite um vetor contendo numeros inteiros: ")))
i = 0

while(i < len(z)):
	if(z[i]%2 != 0):
		z[i] = 0
	i = i + 1

print(z)	