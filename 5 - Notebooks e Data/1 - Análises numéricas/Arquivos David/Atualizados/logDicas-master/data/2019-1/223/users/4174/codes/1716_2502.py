n = int(input("repeticao do termo:"))
soma = 0
i =  0 
exp = 0 
sinal = 1 

while (i < n):
	a = ((2 * i)+1) * (3**exp)
	x = 12**(1/2) * (sinal*1)/a
	soma = soma + x
	i = i + 1
	sinal = sinal *(-1)
	exp = exp + 1
print(round(soma,8))	


