from math import*

x = eval(input("radiano: "))
k = int(input("Quantidade de termos da serie: "))
n = 0
soma = 

while(n < k):
	
	n = n + 1
	sinal = (x**(2 + 2*n)/factorial(2*n))
	sinal = - sinal
	soma  = sinal + sinal
	
print(round(serie, 10))