# Entradas
L = float(input("Lado 1: "))
L2 = float(input("Lado 2: "))
L3 = float(input("Lado 3: "))
print("Entradas: ", L,",", L2,",", L3)
# Condicoes
if (L >= L2 + L3) or (L2 >= L + L3) or (L3 >= L + L2):
	print("Tipo de triangulo: invalido")
elif (L == L2) and (L2 == L3):
	print("Tipo de triangulo: equilatero")
elif (L == L2) or (L == L3) or (L2 == L3):
	print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: escaleno")
	