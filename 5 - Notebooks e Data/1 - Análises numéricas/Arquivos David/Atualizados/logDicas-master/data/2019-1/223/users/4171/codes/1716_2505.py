from math import *

x = (eval(input("Angulo x: ")))
k = int(input("Termos da serie: "))

soma = 0
i = 0

while (i < k):
	
	tg = ((x**(2*i+1)) / factorial(2*i+1))
	
	soma = soma + (-1)**i * tg
	
	i += 1
	
print(round(soma,10))

