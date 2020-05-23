n = int(input("digite n: "))

soma = 0
i = 0 

while(n>0):
	soma = soma + (4/(2*i + 1))*((-1)**i)
	i = i + 1
	n = n - 1
print(round(soma,8))