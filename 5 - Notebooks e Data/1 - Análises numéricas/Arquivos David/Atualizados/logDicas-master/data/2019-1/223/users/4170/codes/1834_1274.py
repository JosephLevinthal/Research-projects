from numpy import*
n = int(input("Insira um numero: "))
m = zeros((n,n), dtype=int)
for i in range(0,n):
	for j in range(0,n):
		m[i,j] = min(i,j)+1
print(m)		