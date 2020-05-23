from numpy import*
nota = array(eval(input("digite as notas: ")))
nome = input("digite os nomes: ")
i = 0
falt = 0
apro = 0
while i <size(nota):
	if nota.any() == -1.0:
		falt = falt + 1
	print(falt)
	