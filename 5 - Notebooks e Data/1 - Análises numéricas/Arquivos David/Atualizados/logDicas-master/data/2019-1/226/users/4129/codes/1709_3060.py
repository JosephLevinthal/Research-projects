dado1 = int(input("Dado 1: "))
dado2 = int(input("Dado 2: "))
r = int(input("Rodadas: "))

danoC = dado1 + dado2 + 1
danoP = (dado1 + dado2 + 1) * r
danoF = dado1 * dado2

if(dado1 < 1 or dado1 >6 or dado2<1 or dado2>6 or r<0):
	print("Entrada invalida")
elif(dado1 + dado2 == 12):
	print("CONSTRICA0")
	print(danoC)
elif(dado1 + dado2 <5):
	print("POLEM")
	print(danoP)
elif(dado1+dado2 >=5 and dado1+dado2 < 12):
	print("FRAQUEZA")
	print(danoF)