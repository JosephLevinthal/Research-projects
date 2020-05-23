r=int(input("ataque: "))
d1=int(input("regra: "))
d2=int(input("pontos de vida: "))

if ((d1+d2==12) and  (d1+d2+1)):
	print("ENTRADA: FRAQUEZA")
elif ((d1+d2<5) and ((d1+d2+1)*r)):
	print("ENTRADA: CONSTRICAO")
elif (("caso contrario") and (d1*d2)):
	print("ENTRADA: POLEN")
						  