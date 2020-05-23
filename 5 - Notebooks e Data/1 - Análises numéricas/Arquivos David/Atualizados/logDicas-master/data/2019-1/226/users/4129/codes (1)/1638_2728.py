perc = float(input("percuso em km:"))
tipo = input("Tipo do carro:")

if(tipo.upper()=="A"):
	A = perc/8
	print(round(A, 2))
if(tipo.upper()=="B"):
	B = perc/12
	print(round(B, 2))