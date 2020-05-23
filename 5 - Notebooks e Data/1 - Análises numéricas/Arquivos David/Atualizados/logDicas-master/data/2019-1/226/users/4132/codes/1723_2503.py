n = int(input("Digite a n: "))
i=1
soma=0
sinal=1
while(i<=n):
	soma = soma + (4/(2*i-1))*sinal
	sinal=sinal*-1
	i=i+1
print(round(soma,8))
	