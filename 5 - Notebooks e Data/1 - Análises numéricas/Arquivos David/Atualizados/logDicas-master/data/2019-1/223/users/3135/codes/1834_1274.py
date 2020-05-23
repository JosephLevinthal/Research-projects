from numpy import*

n= int(input("AAAA:"))

matriarca= zeros((n,n), dtype=int)

for i in range(n):
	for j in range(n):
		matriarca[i,j]= min(i,j)+1
print(matriarca)