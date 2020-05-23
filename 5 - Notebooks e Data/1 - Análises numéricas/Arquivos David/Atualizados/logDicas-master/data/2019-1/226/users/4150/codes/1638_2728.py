percuso = float(input("percuso:"))
carro = input("tipo de carro :")

if ( carro.upper() == "A") :
	a = percuso / 8
	print( round(a, 2))
else:
	b = percuso/12
	print(round(b, 2))