ataque = input("ataque:(FURIA/GRITO/TOQUE)")
dado1 = int(input("numero sorteado: "))
dado2 = int(input("numero sorteado: "))
if ((dado1 < 0) or (dado2 < 0) or (dado1 > 8) or (dado2 > 8)):
	print("Entrada invalida")
elif (ataque == "FURIA"):
	vp = 10 + dado1 + dado2
	print(vp)
elif (ataque == "GRITO"):
	vp = 6 + dado1 + dado2
	print(vp)
elif (ataque == "TOQUE"):
	vp=(dado1 + dado2)**2
	print(vp)

else:
	print("Entrada invalida")
