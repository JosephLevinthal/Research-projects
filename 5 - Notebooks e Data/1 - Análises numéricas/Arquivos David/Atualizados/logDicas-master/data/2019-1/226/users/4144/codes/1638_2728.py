a= float(input("percurso: "))
b= input("tipo de carro: ")
consa = a / 8
consb = a / 12
if (b.upper() == "A"):
	print(round(consa,2))
if (b.upper() == "B"):
	print(round(consb,2))

