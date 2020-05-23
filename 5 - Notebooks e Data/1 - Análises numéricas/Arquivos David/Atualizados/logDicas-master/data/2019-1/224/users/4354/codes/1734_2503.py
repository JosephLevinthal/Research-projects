k = int(input("numero de termos: "))
i = 0
soma = 0
v1 = 1
while(i<k):
	sinal = (-1)**i
	soma = soma + sinal*(4/v1)
	i = i + 1
	v1 = v1 + 2
print(round(soma,8))