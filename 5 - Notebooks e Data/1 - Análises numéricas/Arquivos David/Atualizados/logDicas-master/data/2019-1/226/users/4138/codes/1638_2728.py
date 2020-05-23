p = float(input("insira o percurso:"))
car = input("qual o tipo de carro: (A/B)")

A = p/8
B = p/12

if (car.upper() == "A"):
	print(round(A,2))
else:
	print(round(B,2))