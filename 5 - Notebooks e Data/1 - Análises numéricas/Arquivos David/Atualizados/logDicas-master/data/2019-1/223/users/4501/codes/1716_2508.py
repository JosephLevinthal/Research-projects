num = int(input("No. de aproximacao: "))
cont = 1
a = 3
while(cont < num):
	den = (cont * 2) * (cont * 2 + 1) * (cont * 2 + 2)
	a = a + (-1)**(cont + 1) * 4 / den
	cont = cont + 1
print(round(a, 8))