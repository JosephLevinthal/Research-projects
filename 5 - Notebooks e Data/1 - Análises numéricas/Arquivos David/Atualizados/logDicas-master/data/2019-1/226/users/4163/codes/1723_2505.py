from math import*
x = eval(input("angulo de x: "))
k = int(input(""))

soma =0
i = 0
fim = k-1

while (i<=fim):
	soma = soma + (-1)**i *(x**(2*i+1))/ factorial(2*i+1)
	i = i + 1

print(round(soma, 10))
		
		
	