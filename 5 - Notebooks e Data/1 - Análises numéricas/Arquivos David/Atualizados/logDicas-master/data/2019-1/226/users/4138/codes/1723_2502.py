n = int(input("insira o numero:"))
soma = 0
i = 0
#termo geral = 1*(-1)**i/(2*i+1) * (3)**i
while(n >i):
	tg = 1*(-1)**i
	tg1= (2*i+1) * (3)**i
	
	soma = soma + (tg/tg1)*(12)**0.5
	i = i + 1
print(round(soma,8))