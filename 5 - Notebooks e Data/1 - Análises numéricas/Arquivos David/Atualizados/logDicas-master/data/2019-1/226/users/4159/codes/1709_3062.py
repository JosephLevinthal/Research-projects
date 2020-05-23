po = int(input("pecas de ouro: "))
arm = input("MACHADO, ESPADA ou MARRETA ").upper()
d10 = int(input("valor do dado d10: "))
x = "PO insuficiente"
if(arm=="ESPADA"):
	if(po>=100):
		print(d10*10)
	else:
		print(x)
elif(arm=="MACHADO"):
	if(po>=30):
		print(d10+3)
	else:
		print(x)
elif(arm=="MARRETA"):
	if(po>=50):
		print(d10+5)
	else:
		print(x)
else:
	print("Entrada invalida")