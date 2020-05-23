escala = input("Calsius(C) ou Fahrenheit(F): ")
temperatura = float(input("temperatura: "))

if escala == 'F':
	C = (5/9)*(temperatura - 32)
	print(round(C, 2))
elif escala == 'C':
	F = (9/5*temperatura)+32
	print(round(F, 2))