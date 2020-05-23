N = int(input("digite o numero de termos: "))
soma = 0
for i in range(N):
	soma = soma + 1/(i+1)
print(round(soma,2))