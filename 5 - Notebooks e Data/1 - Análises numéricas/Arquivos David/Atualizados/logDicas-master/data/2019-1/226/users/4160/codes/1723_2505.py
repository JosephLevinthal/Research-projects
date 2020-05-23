from math import *
x = eval(input("Angulo: "))
k = int(input("Numero de termos: "))

soma = 0
i = 0
 
while (i < k ):
	soma = soma + ((-1)**i * (x)**(2*i+1)) / factorial(2*i+1)  
	i = i + 1 
print(round(soma,10))
	