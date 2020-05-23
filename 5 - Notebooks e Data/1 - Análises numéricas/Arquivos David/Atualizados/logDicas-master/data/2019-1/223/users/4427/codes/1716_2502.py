n=int(input("repeticao do termo: "))
soma = 0 #acumulada
i = 0 # contador
expoente = 0 #vc expoente
sinal = 1

while(i<n):
	d = ((2*i)+1)*(3**expoente)
	x = 12**(1/2)*(sinal*1)/d
	soma += x
	i += 1
	sinal = sinal *(-1)
	expoente = expoente + 1
print(round(soma, 8))