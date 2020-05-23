from math import*

x = eval(input("Angulo em radianos:"))
k = int(input("Termos:"))

m = 1    #Potenciação
s = 0  	#Termos
angulo = 0
n = 2

while(s < k):
	angulo = angulo + (((x**m)/factorial(m))* (-1)**n)
	m = m + 2
	s = s + 1
	n = n + 1
print(round(angulo, 10))
	