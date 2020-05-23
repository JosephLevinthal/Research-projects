a = input("Tipo de ataque:").upper()
b = int(input("Quantidade de unidades:"))
if (b<=0):
	print("Entrada invalida")
elif (a=="TERRESTRE"):
	print("DROGON")
	eq = (int(b/150) +1)
	print(eq)
elif (a=="AEREO"):
	print("RHAEGAL")
	eq= (int(b/30) +1) 
	print(eq)
elif (a=="MARITIMO"):
	print("VISERION")
	eq = (int(b/40)+1)
	print(eq)
	