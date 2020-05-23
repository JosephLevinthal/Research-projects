t = input("tipo de ataque: CAUDA/CUSPE/PATADA")
v = int(input("valor:"))
n = int(input("numero de turnos:"))

if(v == 1) or (v == 2) or (v == 3) or (v == 4):
	if(t == "CAUDA"):
		print(n*v)
	elif(t == "CUSPE"):
		z = n * (2*v)
		print(z)
	elif(t == "PATADA"):
		w = 5 - n * (2*n) 
		print(w)
else:
	print("Entrada invalida")
	