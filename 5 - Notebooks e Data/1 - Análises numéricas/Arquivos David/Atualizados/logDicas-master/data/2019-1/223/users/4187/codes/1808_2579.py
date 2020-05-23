calcule = input("Para calcular digite: calcule:" )

x = 1.0
h = 0
if(calcule == "Calcule"):
	for i in range(1,51):
		h = h + (x/i)
		x = x + 2.0
	print(round(h,2))
			
