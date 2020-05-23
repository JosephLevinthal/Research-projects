x = float(input("numero real:"))
k = int(input("numero de termos:"))

cont = 0
acum = 0
s = 1
n = 1

while(cont <  k and -1 < x and x <= +1):
	acum = acum + (x ** n / n) * s
	n = n + 1
	s = s * (-1)
	cont = cont + 1
print(round(acum , 10))
