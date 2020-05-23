n = int(input("digite um numero inteiro positivo: "))
i = 0
soma = 0 
while(i < n):
	x = 1/(i + 1)**2
	soma = soma + x
	i = i + 1
pi = (6*soma)**0.5
print(round(pi, 6))	
	