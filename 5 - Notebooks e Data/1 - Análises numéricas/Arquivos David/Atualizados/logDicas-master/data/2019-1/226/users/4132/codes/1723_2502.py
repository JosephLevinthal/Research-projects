n = int(input("Digite o numero: "))
soma=0
i=0
sinal=1
while(i < n):
	soma = soma + 12**0.5 * ( (1 / ( (2*i+1)*(3**i) ) )*sinal)
	i=i+1
	sinal = sinal*-1
print(round(soma,8))