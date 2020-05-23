acum = 1.5

n = int(input("n termos: "))
cont = n
while (cont >= 0):
	acum = acum * (1 +  (cont / (cont - 2)))
	cont = cont + 1
a = acum * 2
print(round(a, 10))