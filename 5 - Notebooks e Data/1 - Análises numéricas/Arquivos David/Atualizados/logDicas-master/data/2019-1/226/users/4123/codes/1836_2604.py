from numpy import*

mat = array(eval(input()))
n = mat.shape
vet = zeros(n[1])
for x in range(0,n[0]):
	for y in range(0,n[1]):
		vet[y] = mat[x,y]
	print(max(vet))