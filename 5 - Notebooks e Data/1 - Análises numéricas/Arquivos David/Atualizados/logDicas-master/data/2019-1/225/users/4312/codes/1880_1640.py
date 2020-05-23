from numpy import*
vet = array(eval(input("Insira um vetor: ")))

nimpar = 0

for i in range(size(vet)):
	if vet[i]%2 != 0:
		nimpar = nimpar + 1
#print(nimpar)
x = zeros(nimpar, dtype=int)

i=0
for j in range(size(vet)):
	if vet[j]%2 != 0:
		x[i] = j
		i=i+1
	
print(nimpar)
print(x)
	