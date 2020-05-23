n = int(input("numero natural:"))

soma = 0
d = 1
i = 0
aux = 1

while(i < n):
	soma = soma + (aux * (4/d))
	if(aux == 1):
		aux = -1
	else:
		aux = 1
	i = i + 1
	d = d + 2
print(round(soma,8))
	
	