n = int(input("digite o valor de n: "))
i = 0
soma = 0
while(n>i):
	x = (2*i+1) * 3**i
	y = 1 * (-1)**i
	soma = soma + ((12)**0.5) * (y/x)
	i= i +1
print(round(soma,8))