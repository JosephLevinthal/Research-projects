v = int(input("quantidade de repeticoes: "))
soma = 0
i = 0
while(i<v):
	soma += 4*(((-1)**i)/(2*i+1))
	i = i + 1

print(round(soma,8))