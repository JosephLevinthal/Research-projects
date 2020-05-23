x=input("tipo de ataque:")
y=int(input("quantidade de unidades:"))
if(x==terrestre):
		y=150
		print("DRAGON",1)
	if(x==aereo):
		y=30
	   print("RHAEGAL",2)
	if(x==maritimo):
		y=40
		print("VISERION",3)
else:
	print("Entrada invalida")
	
		