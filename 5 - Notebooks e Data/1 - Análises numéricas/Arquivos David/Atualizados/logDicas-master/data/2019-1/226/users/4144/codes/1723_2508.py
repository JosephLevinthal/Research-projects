n = int(input("digite o valor de n: "))
i = 1
soma = 3
while(n > i):
	x = (2*i)*(2*i+1)*(2*i+2)
	soma = soma + (4/x) * ((-1)**(i+1))
	i= i+1
print(round(soma,8))