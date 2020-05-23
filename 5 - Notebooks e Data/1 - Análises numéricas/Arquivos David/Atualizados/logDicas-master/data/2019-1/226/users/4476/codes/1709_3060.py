d1 = int(input("primeiro valor sorteado: "))
d2 = int(input("segundo valor sorteado: "))
r = int(input("numero de rodadas: "))

if (d1<1) or (d1>6) or (d2<1) or (d2>6) or (r<0):
	print("Entrada invalida")
elif ((d1 + d2) == 12):
	print("CONSTRICAO")
	print(d1 + d2 + 1)
elif ((d1 + d2) < 5):
	print("POLEN")
	print((d1 + d2 + 1)*r)
else:
	print("FRAQUEZA")
	print(d1*d2)
	