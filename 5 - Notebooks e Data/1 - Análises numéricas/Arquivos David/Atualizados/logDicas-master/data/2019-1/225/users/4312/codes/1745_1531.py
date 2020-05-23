from math import*
ang = eval(input("Insira o angulo: "))
k = int(input("Quant. dos termos: "))

i = 0
cont = 0
c = 0
while(i < k):
	cont = cont + ((-1)**i * (ang**c / factorial(c)))
	c = c + 2
	i = i + 1

print(round(cont, 10))