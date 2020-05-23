km = float(input("Digite o percurso: "))
carro = input("Tipo do carro: ")
A = km/8
B = km/12
if (carro == "A"):
	print(round(A,2))
else: 
	print(round(B,2))