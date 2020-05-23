ataque = input("digite o atque: ")
d = int(input("dado lancado: "))
d2 = int(input("dado 2 lancado: "))
ataque = ataque.upper()
if(ataque == "FURIA" and 2 <= d+d2 <= 16 ):
	s_dado = d + d2
	dano = 10 + s_dado
	print(dano)
elif(ataque == "GRITO" and 2 <= d+d2 <= 16):
	s_dado = d + d2
	dano = 6 + s_dado
	print(dano)
elif(ataque == "TOQUE" and 2 <= d+d2 <= 16):
	s_dado = d + d2
	dano = s_dado**2
	print(dano)
else:
	print("Entrada invalida")



