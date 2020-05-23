n = int(input("insira o numero:"))
soma = 3
i = 1
#termogeral = 4 * (-1)**i + 1/(2*i) * (2*i + 1) * (2 i +2)

while(n > i):
	tg = (2*i) * (2*i + 1) * (2*i +2)
	soma = soma + (4 * (-1)**(i + 1))/tg
	i = i + 1

print(round(soma,8))