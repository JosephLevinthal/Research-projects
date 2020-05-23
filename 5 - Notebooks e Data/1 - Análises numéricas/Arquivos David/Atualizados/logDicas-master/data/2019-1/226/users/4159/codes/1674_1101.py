c = float(input("consumo: "))
i = input("tipo de instalacao: ").upper()
if(((i=="R")and(i=="C")and(i=="I")and(c>=0))):
	if(i=="R"):
		if(c<=500):
			t = 0.44
		else:
			t = 0
		
