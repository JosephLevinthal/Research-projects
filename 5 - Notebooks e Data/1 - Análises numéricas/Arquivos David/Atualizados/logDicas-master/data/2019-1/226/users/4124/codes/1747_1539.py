x = float(input("Numero real x: "))
k = int(input("Numero de termos da serie: "))
i = 0
soma = 0
while(k >= i+1):
	soma = soma + ((x ** i) * (-1)**i)
	i = i + 1
print(round(soma, 7))