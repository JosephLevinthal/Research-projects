a=input("Qual o ataque?: ")
v=int(input("Qual o valor sorteado?: "))
t=int(input("Qual o numero de turnos?: "))
if (v < 1 or v > 4) or (not(a == "CAUDA" or not a == "CUSPE" or not a == "PATADA")):
	print("Entrada invalida")
elif (a=="CAUDA"):
	print(v*t)
elif (a=="PATADA"):
	print((2*v-5)*t)
elif (a=="CUSPE"):
	print((2*v)*t)
	
	