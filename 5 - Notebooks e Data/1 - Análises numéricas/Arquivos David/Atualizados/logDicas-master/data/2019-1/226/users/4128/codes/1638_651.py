al = float(input("metros"))
s = input("sexo? (M/F)")

if(s.upper() == "M"):
	ph = (72.7 * al) - 58
	print(round(ph,2))
else:
	pm = (62.1* al) - 44.7
	print(round(pm,2))
	
	


#nota = float(input("nota do abencoado: "))
#boni = input("bonificacao? (S/N) ")

#if(boni.upper() == "S"):
	#print(nota*1.1)
#else:
	#print(nota)