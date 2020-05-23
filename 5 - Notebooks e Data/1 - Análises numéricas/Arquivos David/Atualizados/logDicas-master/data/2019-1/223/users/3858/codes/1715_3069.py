nomeAtk = input()
dado1 = int(input())
dado2 = int(input())

if(dado1>=1 and dado2>=1 and dado1<=8 and dado2<=8):
	if(nomeAtk=="FURIA" or nomeAtk=="TOQUE" or nomeAtk=="GRITO"):
		if(nomeAtk=="FURIA"):
			DANO = 10 + dado1 + dado2
		elif(nomeAtk=="GRITO"):
			DANO = 6 + dado1 + dado2
		elif(nomeAtk=="TOQUE"):
			DANO = (dado1 + dado2)**2
		print(DANO)
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
	