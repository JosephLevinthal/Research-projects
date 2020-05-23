pc= float(input("qual o valor do produto?"))
pgm= float(input("qual o valor do pagamento?"))

if (pc>pgm):
	print("Falta",round(pc-pgm,2))
else:
	print("Troco de",round(pgm-pc,2))

