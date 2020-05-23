nota = float(input("nota: "))
mamata = input("tem bonificacao?(S/N) ").upper()
if(mamata == "S"):
	print(nota+nota/10)
else:
	print(nota)