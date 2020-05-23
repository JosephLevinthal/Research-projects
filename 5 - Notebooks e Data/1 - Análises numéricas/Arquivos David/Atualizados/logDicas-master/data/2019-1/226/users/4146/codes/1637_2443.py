from math import*

raio = float(input("Raio: "))
altura = float(input("Altura: "))
opcao = input("1/2: ")

if (opcao == "1"):
	V = ((pi*(altura**2)) * (3*raio - altura))/3
else:
	V = ((4*pi*(raio**3))/3) - ((pi*(altura**2)) * (3*raio - altura))/3
	
print(round(V, 4))	