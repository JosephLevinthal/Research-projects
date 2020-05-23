n = int(input("n: "))

i = 0
b = 2
soma = 0

while (i < n-1):

	tg = (4 / ( b * (b+1) * (b+2) ))
	
	soma = soma + (-1)**i * tg 
	
	b += 2
	i += 1
	
soma += 3
print(round(soma,8))
