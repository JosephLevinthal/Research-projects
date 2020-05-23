N = int(input("digite o numero de termos: "))
soma = 0
for i in range(N):
	sinal = (-1)**i
	soma = soma + sinal*(1/(i+1))
print("H =",round(soma,6))