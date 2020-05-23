a = float(input("Numero de habitantes de uma cidade A: "))
b = float(input("Numero de habitantes da uma cidade B: "))
A = float(input("Percentual de crescimento populacional da cidade A: "))
B = float(input("Percentual de crescimento populacional da cidade B: "))

ano = 0

while (a <= b):
	a = a + A/100 *a
	b = b + B/100 *b
	ano= ano+1
print(ano)
		