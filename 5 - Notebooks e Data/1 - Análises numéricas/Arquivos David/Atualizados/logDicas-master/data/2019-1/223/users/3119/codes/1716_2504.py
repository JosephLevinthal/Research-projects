a = int(input("Quantidade inicial de copias do virus: "))
b = int(input("Quantidade inicial de leucocitos no sangue: "))
c = int(input("Percentual de multiplicacao diaria do virus: "))
d = int(input("Percentual de multiplicacao diaria dos leucocitos: "))

dia = 0

while(a * 2 > b):
	a = (a * (c/100)) + a
	b = (b * (d/100)) + b
	dia = dia + 1
print(dia)
	