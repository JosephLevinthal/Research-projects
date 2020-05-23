q = float(input("quantidade de oruro: "))
n = input("nome da armadura: ")
d = int(input("fator de destreza: "))
if((d > 8)or(d<=0)):
	print("Entrada invalida")
elif((q>=200)and(n=="INTEIRA")):
	h = 30 * d - 20
	print(h)
elif((n=="MALHA")and(q>=50)):
	h = 15 * d -1
	print(h)
elif((n=="PLACA")and(q>=100)):
	h = 20 * d -18
	print(h)
else:
	print("PO insuficiente")