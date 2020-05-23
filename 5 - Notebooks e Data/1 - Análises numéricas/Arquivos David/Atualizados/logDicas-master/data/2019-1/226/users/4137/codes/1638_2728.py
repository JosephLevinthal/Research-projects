km = float(input("Percuso em km:"))
tp = input("Tipo do carro, A ou B:")

if(tp.upper() == "A"):
	msg = km/8
else:
	msg = km/12
print(round(msg, 2))	