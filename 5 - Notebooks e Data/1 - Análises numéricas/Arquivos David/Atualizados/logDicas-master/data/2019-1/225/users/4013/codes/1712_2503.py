n = int (input("numero de termos:"))

a = 1
s = 1
acum = 0
cont = 0

while(cont < n):
	acum = acum + (4 / a) * s
	a = a + 2
	s = s * (-1)
	cont = cont + 1
print(round(acum , 8))
	