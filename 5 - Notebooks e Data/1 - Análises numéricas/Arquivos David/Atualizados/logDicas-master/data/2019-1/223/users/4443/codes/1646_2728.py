#Percurso da vaigem em Km e tipo de carro
km = float(input("digite o percurso: "))
carro = input("digite o tipo de carro (A ou B): ")

#consumo estimado:
A = km/8
B = km/12

if(carro == "A"):
	print(round(A, 2))

else:
	print(round(B, 2))	