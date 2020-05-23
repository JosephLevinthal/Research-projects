n = int(input('Digite n: '))
soma = 3
cont = 1
sinal = 1
d1 = 2
d2 = 3
d3 = 4 
while (cont < n):
	soma = soma + (4/(d1*d2*d3)) * sinal
	sinal = sinal * (-1)
	d1 = d1 + 2
	d2 = d2 + 2
	d3 = d3 + 2
	cont = cont + 1
print(round(soma,8))
	
	
	
