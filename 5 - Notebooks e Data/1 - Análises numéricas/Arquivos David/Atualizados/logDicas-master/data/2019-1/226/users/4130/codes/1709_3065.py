x = input("Parte que se deferiu o golpe: ").upper()
y = int(input("Numero de vida perdidos: "))
z = int(input("Numero de turnos: "))

if(x == "CAUDA"):
	w = (y * z)
	print(w)
elif(x == "CUSPE"):
	w = (2 * (y * z))
	print(w)
elif(x == "PATADA"):
	w = ((2 * y) - (5 * z))
	print(w)
elif(x == "cauda") or (x == "cuspe") or (x == "patada") or (y > 4):
	print("Entrada invalida")