virus = int(input("Virus :"))
leucocitos = int(input("Leucocitos:"))
pvirus = int(input("Percentual diario de multiplicacao dos virus:"))
pleuco = int(input("Percentual diario de multiplicacao dos leucocitos:"))

dias = 0
pvirus = pvirus/100
pleuco = pleuco/100

while (leucocitos < 2*virus):
	dias = dias + 1
	virus = virus + (virus*pvirus)
	leucocitos = leucocitos + (leucocitos*pleuco)
print(dias)