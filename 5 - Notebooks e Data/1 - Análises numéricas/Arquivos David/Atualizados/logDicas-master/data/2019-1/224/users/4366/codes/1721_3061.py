ataque=input("o tipo de ataque TERRESTRE,AEREO ou MARITIMO:")
quantidade=int(input("quantidade de unidades:"))
ataque=ataque.upper()
if(ataque=="TERRESTRE") and (quantidade>0):
	msg=quantidade-150
	print("DROGON")
	print(msg)
elif(ataque=="AEREO") and (quantidade>0):
	msg=quantidade-30
	print("RHAEGAL")
	print(msg)
elif(ataque=="MARITIMO") and (quantidade>0):
	msg=quantidade-
	print("VISERION")
	print(msg)
else:
	print("Entrada invalida")
	


	
	
	
	