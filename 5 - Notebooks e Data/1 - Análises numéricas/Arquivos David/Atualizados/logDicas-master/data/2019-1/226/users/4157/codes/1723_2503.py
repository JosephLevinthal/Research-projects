n = int(input("digite o numero:"))
soma = 0 
i = 0
while(i<n):
	soma = soma  + ((-1)**i)*(4/(2*i+1))
	i = i + 1
print(round(soma,8))