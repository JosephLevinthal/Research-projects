a = float(input("sua altura: "))
b = input("sexo: ")
			 
ph = (72.7*a)-58
pm = (62.1 * a) - 44.7
			
if (b.upper() == "M"):
	print(round(ph, 2))
else:
	print(round(pm, 2))
			 