from numpy import*

n= int(input("Digite um numero: "))

mat = zeros((n,n), dtype = int)

for i in range(n):
	for j in range (n):
		if i > j:
			mat[i,j] = j +1
		elif i < j:
			mat[i,j] = i + 1
		elif i == j:
			mat[i,j] = i + 1
print(mat)