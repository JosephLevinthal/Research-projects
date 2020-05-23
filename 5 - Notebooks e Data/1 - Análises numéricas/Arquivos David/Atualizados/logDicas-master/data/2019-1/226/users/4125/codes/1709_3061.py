x = input("digite o tipo de ataque: ").upper()
y = int(input("digite quantas unidades: "))
if(x == "TERRESTRE")and(y>0):
	dragao = "DROGON"
	baforada = 150
	z = y/baforada
	print(dragao)
	if(y<150):
		z1 = z + 1
		print(int(z1))
	elif(y>=150):
		z1 = z + 1 
		print(int(z))
	
elif(x == "AEREO")and(y>0):
	dragao = "RHAEGAL"
	baforada = 30
	z = y/baforada
	print(dragao)
	if(y<30):
		z1 = z + 1
		print(int(z1))
	elif(y>=30):
		z1 = z + 1
		print(int(z1))
elif(x == "MARITIMO")and(y>0):
	dragao = "VISERION"
	baforada = 40
	z = y/baforada
	print(dragao)
	if(y<40):
		z1 = z + 1 
		print(int(z1))
	elif(y>=40):
		z1 = z + 1
		print(int(z1))
else:
	print("Entrada invalida")