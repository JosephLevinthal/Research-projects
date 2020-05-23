ta=input("tipo de ataque (CAUDA/CUSPE/PATADA): ").upper()
valor=int(input("valor sorteado: "))
nt=int(input("numero de turnos:"))
		  
if ((valor != 1 ) and ( valor != 2 ) and ( valor != 3 ) and ( valor != 4 )):
	x="Entrada invalida"
	print(x)
elif ( valor == 1):
	if ( ta == "CAUDA"):
		x = valor
	elif ( ta == "PATADA"):
		x = 2*valor-5
	elif ( ta == "CUSPE"):
		x = 2*valor*nt
elif ( valor == 2):
	if ( ta == "CAUDA"):
		x = valor
	elif ( ta == "PATADA"):
		x = 2*valor-5
	elif ( ta == "CUSPE"):
		x = 2*valor*nt
elif ( valor == 3):
	if ( ta == "CAUDA"):
		x = valor
	elif ( ta == "PATADA"):
		x = 2*valor-5
	elif ( ta == "CUSPE"):
		x=2*valor*nt
elif ( valor == 4):
	if ( ta == "CAUDA"):
		x = valor
	elif ( ta == "PATADA"):
		x = 2*valor-5
	elif( ta == "CUSPE"):
		x = 2*valor*nt
	print(x)
	

	
	
	
	