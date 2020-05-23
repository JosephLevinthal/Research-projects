from numpy import*
vet = array(eval(input("Numeros: ")))
i = 0
x = 0

while(i != size(vet)):
	x = x + ((vet[i])**(1/6))
	i = i + 1

n = size(vet)
M = ( x / n )**6
print(round(M, 2))