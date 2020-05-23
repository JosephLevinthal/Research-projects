n = int(input("numero de termos:"))

acum = 3
cont = 1
s = 1
a = 2

while (cont < n):
	acum = acum + (4 / (a * (a + 1) * (a + 2))) * s 
	s = s * (-1)
	a = a + 2
	cont = cont + 1
print(round(acum , 8))