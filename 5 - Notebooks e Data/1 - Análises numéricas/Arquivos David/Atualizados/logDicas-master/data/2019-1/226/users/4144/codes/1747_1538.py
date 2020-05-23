x = float(input("digite o valor de x: "))
k = int(input("digite o valor de k: "))
i = 0
soma = 0
while(i<k):
	soma = soma + ((x**(2*i)) * (-1)**i)
	i = i + 1
print(round(soma,8))