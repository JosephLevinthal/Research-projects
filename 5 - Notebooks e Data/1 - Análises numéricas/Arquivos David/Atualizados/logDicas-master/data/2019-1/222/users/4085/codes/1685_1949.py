na = int(input("escreva o numero apostado: "))
ns = int(input("escreva o numero sorteado: "))
d1 = na // 10
d2 = na % 10 
d3 = ns //10
d4 = ns % 10
if (ns == na):
	print ("Ganhou R$ 100.000,00")
elif ((d4 == d1) and (d3 == d2)):
	print ("Ganhou R$ 50.000,00")
elif ((d1 == d3) or (d1 == d3) or (d2 == d3) or (d2 == d4)):
	print ("Ganhou R$ 1.000,00")
else:
	print ("Perdeu")