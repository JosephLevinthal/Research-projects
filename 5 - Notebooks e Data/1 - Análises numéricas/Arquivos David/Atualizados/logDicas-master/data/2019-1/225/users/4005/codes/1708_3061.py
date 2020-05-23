t=input("tipo de ataque:")
q=int(input("quantidade de unidades a seren destruidas:"))
if(t=="TERRESTRE"):
	print("DROGON")
	print(int(q/150)+(1))
elif(t=="AEREO"):
	print("RHAEGAL")
	print(int(q/30)+(1))
elif(t=="MARITIMO"):
	print("VISERION")
	print(int(q/40)+(1))
else:
	print("Entrada invalida")
	