n = int(input("digite o valor de n: "))
i = 0
soma = 0
while(n > i):
	x = 2*i+1
	soma = soma + (4/x) * (-1)**(i)
	i= i+1
print(round(soma,8))