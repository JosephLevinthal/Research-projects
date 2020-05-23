from numpy import*

vet = array(eval(input("vetor:")))
g = 0

for e in range(size(vet)):
	if(vet[e] % 2 != 0):
		g+=1
v = zeros(g,dtype=int)
h = 0
for e in range(size(vet)):
	if(vet[e]%2 != 0):
		v[h]=vet[e]
		h+=1
		
print(v)
		
		