from numpy import*

j = array(eval(input()))

n = 0

for i in range(size(j)):
	if j[i]<=50:
		n = n + 1
print(n)
vet = zeros(n, dtype=int)
c=0
g=0

for i in range(size(j)):
	if j[i]<=50:
		vet[g] = j[c]
		c = c + 1 
	g = g + 1
print(vet)