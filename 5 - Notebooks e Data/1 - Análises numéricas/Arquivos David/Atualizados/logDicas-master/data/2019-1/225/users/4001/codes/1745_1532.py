from math import *
x = float(input("x: "))
k = int(input("n: "))
cont = 0 #contadora
soma = 0 #acumuladora
i = 1 #expoente
d = 1 #var. do denominador
while (cont < k):
	sinh = (x**i)/factorial(d)
	soma = soma + sinh
	cont = cont + 1
	i = i + 2
	d = d + 2
print(round(soma, 9))	
	