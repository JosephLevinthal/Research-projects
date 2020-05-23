J = int(input("No. apostado: "))
L = int(input("No. sorteado: "))

if ( J == L):
	print("Ganhou R$ 100.000,00")
elif (J // 10 == L % 10) and (J % 10 == L // 10):
	print("Ganhou R$ 50.000,00")
elif (J // 10 == L // 10) or (J // 10 == L % 10) or (J % 10 == L // 10) or (J % 10 == L % 10):
	print("Ganhou R$ 1.000,00")
else: 
	print("Perdeu")