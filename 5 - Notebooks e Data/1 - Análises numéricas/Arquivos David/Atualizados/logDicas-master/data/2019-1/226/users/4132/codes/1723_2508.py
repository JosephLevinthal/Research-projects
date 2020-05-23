n = int(input("Digite n: "))
soma = 3.0
i=1
sinal=1
while(i<n):
	soma =  soma + (4/((2*i)*(2*i+1)*(2*i+2)))*sinal
	i=i+1
	sinal = sinal*-1
	
print(round(soma,8))
	
	