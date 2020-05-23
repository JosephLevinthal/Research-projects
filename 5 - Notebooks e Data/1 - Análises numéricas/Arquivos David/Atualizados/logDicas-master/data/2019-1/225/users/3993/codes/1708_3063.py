po = float(input("pecas de ouro: "))
n = input("nome da armadura: ")
f = int(input("fator de destreza: "))


if ( po >= 200):
	d = 30*f - 20
	a = ("INTEIRA")
	print(d)
elif ( po >= 50):
	d = 15*f - 1
	a = ("MALHA")
	print(d)
elif ( po >=100):
	d = 20*f - 18
	a = ("PLACA")
	print(d)
elif (po < 50):
	print("PO insuficiente")
else:
	print("Entrada invalida")
		
		
	
	
		


		  