n = int(input("Repeticao: "))
soma = 0
exp = 0 
i = 0
sinal = 1

while(i < n):
	d = ((2*i)+1)*(3**exp)
	x = 12**(1/2)*(sinal * 1)/d
	soma = soma + x
	i = i + 1
	sinal = sinal*(-1)
	exp = exp + 1
print(round(soma , 8))
	