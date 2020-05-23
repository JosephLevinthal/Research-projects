x = int(input("idade: "))
y = float(input("IMC: "))
print("Entradas:", x , "anos", "e", "IMC", y)

if(x < 45 and x > 0 and y < 22 and y > 0):
	print("Risco: Baixo")
else:
	if(x < 45 and x > 0 and y >= 22.0):
		print("Risco: Medio")
	elif(x >= 45 and y < 22.0 and y > 0):
		print("Risco: Medio")
	elif(x >= 45 and y >= 22.0):
		print("Risco: Alto")
	elif((x <= 0) or (x > 130) or (y <= 0)):
		print("Dados invalidos")