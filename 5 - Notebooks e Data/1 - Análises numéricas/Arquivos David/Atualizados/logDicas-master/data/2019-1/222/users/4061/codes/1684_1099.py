ladoA = float(input("digite o lado A: "))
ladoB = float(input("digite o lado B: "))
ladoC = float(input("digite o lado C: "))

print("Entradas: ", ladoA, ",", ladoB, ",", ladoC)

if ((ladoB - ladoC) < ladoA and ladoA < (ladoB + ladoC) and (ladoA - ladoC) < ladoB and ladoB < (ladoA + ladoC) and (ladoA - ladoB) < ladoC and ladoC < (ladoA + ladoB)):
	if (ladoA == ladoB and ladoB == ladoC):
		print("Tipo de triangulo: equilatero")
	elif((ladoA == ladoB and ladoA != ladoC) or (ladoC == ladoA and ladoC != ladoB) or (ladoC == ladoB and ladoB != ladoA)):
		print("Tipo de triangulo: isosceles")
	elif(ladoA != ladoB and ladoA != ladoC and ladoB != ladoC):
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")


