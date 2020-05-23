from math import*

x = eval(input(" Radiano: "))
nt = int(input(" Numero de termos: "))
sinal = x
cont = 0
soma = 0

while ( cont < nt ):
	
	soma = soma + (sinal**(2*cont+1))/factorial(2*cont + 1)
	sinal = - sinal 
	cont = cont + 1
	
print(round( soma, 10))