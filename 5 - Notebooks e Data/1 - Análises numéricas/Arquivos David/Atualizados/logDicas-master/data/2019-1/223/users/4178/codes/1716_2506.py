anos = 0 
quant = float(input("Quant "))
porcc = int(input("Porce "))/100
porcr = float(input("Retirada  "))

while ( 0 < quant < 12000 ):
	xx1 = quant * porcc
	quant = quant + xx1
	quant = quant - porcr
	anos = anos + 1
	if (quant <= 0):
		print("EXTINCAO")
	else :
		print("LIMITE")
print(anos)		

