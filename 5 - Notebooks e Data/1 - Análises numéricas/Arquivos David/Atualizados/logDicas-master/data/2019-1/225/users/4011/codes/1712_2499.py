from math import*
n = int(input("Numero de Termos: "))

acum = 0
cont = 0

while ( cont < n):
	
	acum = acum + 1/(factorial(cont))
	cont = cont + 1
	
print(round(acum, 8))