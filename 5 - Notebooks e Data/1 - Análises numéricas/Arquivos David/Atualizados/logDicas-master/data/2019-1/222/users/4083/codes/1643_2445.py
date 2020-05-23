qual = input("digite a escala: ")
temperatura = float(input("DIGITE A TEMPERATURA: "))
c = (5/9)*(temperatura - 32)
f = (9*temperatura + 160)/5
if  (qual == "C"):
		print(round(f, 2))
		
		
if  (qual == "F"):
	  print(round(c, 2))