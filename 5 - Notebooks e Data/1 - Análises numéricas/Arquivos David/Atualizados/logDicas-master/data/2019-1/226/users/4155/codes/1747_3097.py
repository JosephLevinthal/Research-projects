n = int(input("n: "))
soma = 0
i = 0
while(n!=0):
	soma = soma + n*31 - 6*n
	i = i + 1
	n = int(input("n:"))
print(soma)
