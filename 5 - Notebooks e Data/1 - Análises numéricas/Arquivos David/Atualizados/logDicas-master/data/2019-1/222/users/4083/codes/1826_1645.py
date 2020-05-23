from numpy import*
vet = array(eval(input("digite o vetor: ")))

b = 0
for i in range(size(vet)):
	if	(vet[i] >= 2000):
		b = b + 1
print(b)
g = 0
a = zeros(b, dtype=int)
for h in range(size(vet)):
	
	if	(vet[h] >= 2000):
		a[g] = a[g] + h
		g = g + 1
		
print(a)