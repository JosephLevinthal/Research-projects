from math import*
x = eval(input("angulo:"))
t = int(input("numero de termos:"))

cont = 0
acum = 0
s = 1
n = 1

while (- pi <= x and x <= +pi and cont < t):
	
	acum = acum + (x ** n / factorial(n)) * s
	cont = cont + 1
	s = s * (-1)
	n = n + 2
	
print(round(acum , 10))