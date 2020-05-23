ta=input("tipo de ataque: ").upper()
v=int(input("valor do dado: "))
nt=int(input("numero de turnos: "))

if(1 <= v <= 4):
	if(ta=="CAUDA"):
		N=v*nt
		print(N)
	elif(ta=="CUSPE"):
		N=v*nt
		print(2*N)
	elif(ta=="PATADA"):
		N=v*nt
		print((2*N)-5)
else:
	print("Entrada invalida")
		