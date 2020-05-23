atq = input("tipo de atq:").upper()
qdu = int(input("numero de unidades:"))

if(qdu < 0):
	print("Entrada invalida")			 
elif(atq == "TERRESTRE"):
	print("DROGON")
	x = qdu/150
	z = int(x + 1)
	print(z)
elif(atq == "AEREO"):
	print("RHAEGAL")
	x = qdu/30
	z = int(x + 1)
	print(z)
elif(atq == "MARITIMO"):
	print("VISERION")
	x = qdu/40
	z = int(x +1)
	print(z)
else:
	print("Entrada invalida")