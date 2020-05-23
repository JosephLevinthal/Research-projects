a = int(input("numero de habitantes da cidade A: "))
b = int(input("numero de habitantes da cidade B: "))
pa = float(input("Percentual de crescimento populaciuonal da cidade A: "))
pb = float(input("Percentual de crescimento populacional da cidade B: "))

t = 0

while (a < b):
	x = (a * pa) / 100
	a = a + x
	y = (b * pb) / 100
	b = b + y
	t = t + 1
print(t)	