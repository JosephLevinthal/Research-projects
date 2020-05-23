ataque = input("FURIA/GRITO/TOQUE? ").upper()
dado1 = int(input("VALOR SORTEADO: "))
dado2 = int(input("VALOR SORTEADO: "))

s = dado1 + dado2

if (( (1 <= dado1) and ( dado1 <= 8) ) and ( (1 <= dado2) and (dado2 <= 8) )):
	if ( ataque == "FURIA"):
		dt = 10 + ( s )
		print( dt )
	elif ( ataque == "GRITO"):
		dt = 6 + ( s )
		print( dt )
	elif ( ataque == "TOQUE"):
		dt = ( s )**2
		print( dt )
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
		