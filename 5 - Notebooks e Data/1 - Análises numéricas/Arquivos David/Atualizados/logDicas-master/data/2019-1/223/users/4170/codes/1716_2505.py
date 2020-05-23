from math import*
x = eval(input("Digite o angulo: "))
k = int(input("Digite o numero de termos: ")) -1
soma = 0
cont = 0
while(cont <= k):
	f = ((((-1)**cont))*(x**(2*cont+1))/(factorial(2*cont+1))) 
	soma = soma + f
	cont = cont + 1
print(round(soma,10))	
	