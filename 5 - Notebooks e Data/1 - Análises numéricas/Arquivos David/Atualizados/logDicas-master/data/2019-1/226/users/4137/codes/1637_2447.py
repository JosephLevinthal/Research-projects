pcr = float(input("Qual o valor do produto:"))
pgm = float(input("Valor pago:"))

if (pcr > pgm):
	x = round(pcr - pgm, 2)
	msg = "Falta" + " " + str(x)
	
else:
	x = round(pgm - pcr, 2)
	msg = "Troco" + " " + "de" + " " + str(x)
	
print(msg)