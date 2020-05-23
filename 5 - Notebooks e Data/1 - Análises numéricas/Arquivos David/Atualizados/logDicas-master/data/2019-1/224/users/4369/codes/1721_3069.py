na = str(input("Digite o nome do ataque: ").upper())
vd1 = int(input("Digite o valor do dado 1 de 8 faces: "))
vd2 = int(input("Digite o valor do dado 2 de 8 faces: "))

if((0 < vd1 <= 8 and 0 < vd2 <= 8) and na == "FURIA".upper()):
	d = 10 + vd1 + vd2
	print(d)
elif(na == "GRITO".upper()):
	d = 6 + vd1 + vd2
	print(d)
elif(na == "TOQUE".upper()):
	d = (vd1 + vd2) ** 2
	print(d)
else:
	print("Entrada invalida")
	