total = float(input(""))
qtdru = int(input(""))
vru = float(input(""))
qtdonibus = int(input(""))
vonibus = float(input(""))

if ( (qtdru* vru) + (qtdonibus * vonibus) <= total):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")