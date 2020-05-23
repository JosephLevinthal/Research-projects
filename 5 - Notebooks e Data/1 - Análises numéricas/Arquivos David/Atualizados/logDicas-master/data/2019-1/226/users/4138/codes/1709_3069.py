x = input("nome do ataque da banshee:").upper()
y = int(input("insira o numero do dado 1:"))
z = int(input("insira o  numero do dado 2:"))

if( y >= 1 and z <= 8 and x == "FURIA"):
	print(10 + z + y)
elif(y >=1 and y <=8 and x == "GRITO"):
	print(6 + z + y)
elif(y >= 1 and y <= 8 and x == "TOQUE"):
	a = (y + z)**2
	print(a)
else:
	print("Entrada invalida")