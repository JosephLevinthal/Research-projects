from math import*
k = float(input("numero natural k :"))

acum = 0
cont = 0

while (cont < k ):
	acum = acum + (1 / (factorial(cont)))
	cont = cont + 1
print(round(acum , 8))