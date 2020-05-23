x = (input("digite o ataque realizado por cornugon: (cauda,patada,cuspe)")).upper()
y = int(input("digite o valor do dado de 1 a 4: "))
w = int(input("numero de turnos q o persnagem fica ferido: "))


if (x.upper() == "CAUDA"  or  x.upper() == "CUSPE"  or  x.upper() == "PATADA"):
	if y > 0  and y <= 4  and w > 0:
		if x.upper() == "CAUDA":
			print(y*w)
		elif x.upper() == "CUSPE":
			print((2*y)*w)
		elif x.upper() == "PATADA":
			print(((2*y)-5)*w)
	else:
		print("Entrada invalida")
else: 
	print("Entrada invalida")