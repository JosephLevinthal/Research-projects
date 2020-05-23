n = int(input("insira o numero:"))
soma = 0
i = 0
#termogeral = 4*(-1)**i/(2*i + 1)

while(n > i):
	soma = soma + 4*(-1)**i/(2*i + 1)
	i = i + 1
	
print(round(soma,8))