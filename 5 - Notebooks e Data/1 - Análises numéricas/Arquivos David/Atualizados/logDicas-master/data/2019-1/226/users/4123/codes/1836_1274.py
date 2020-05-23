from numpy import*
k = int(input())
vet = ones((k,k),dtype = int)
i = j = 0
it = array([i,j])
while j < k:
	it[0] = i+1
	it[1] = j+1
	while i < k:
		if i>j:
			vet[(i),(j)] = j+1
		else:
			vet[(i),(j)] = i+1
		i += 1
	j += 1
	i = 0
print(vet)