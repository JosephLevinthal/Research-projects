a = int(input("Numero de habitantes cidade A: "))
b = int(input("Numero de habitantes cidade B: "))
pa = float(input("Percentual de crescimento populacional da cidade A: "))
pb = float(input("Percentual de crescimento populacional da cidade B: "))
anos = 0
while (a < b):
	cresa = a * (pa/100)
	a = a + cresa
	cresb = b * (pb/100)
	b = b + cresb
	anos = anos + 1
print (anos)