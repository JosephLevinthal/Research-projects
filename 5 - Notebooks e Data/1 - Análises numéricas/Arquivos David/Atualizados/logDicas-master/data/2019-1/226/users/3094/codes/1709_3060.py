d1 = int(input("valor dado 1: "))
d2 = int(input("valor dado 2: "))
r = int(input("rodada: "))

if(d1 <= 0 or d1> 6 or d2<=0 or d2>6):
	a = "Entrada invalida"
	print(a)
elif(d1 + d2 == 12):
	a = "CONSTRICAO"
	dano = d1 + d2 + 1
	print(a)
	print(dano)
elif(d1 + d2 < 5):
	a = "POLEN"
	dano = (d1 + d2 + 1) * r
	print(a)
	print(dano)
else:
	a = "FRAQUEZA"
	dano = d1 * d2
	print(a)
	print(dano)
	#if(a == "CONSTRICAO"):
		#dano = d1 + d2 + 1
	#elif(a == "POLEN"):
	#	dano = (d1 + d2 + 1)*r
	#elif(a == "FRAQUEZA"):
		#dano = d1 * d2
#print(dano)






