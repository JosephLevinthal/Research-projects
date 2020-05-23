valor=float(input("valor disponivel"))
tickets=float(input("quantidade "))
valortick=float(input("valor dos tickets"))
onibus=float(input("onibus"))
valoron=float(input("valor onibus"))

if (valor> ((tickets*valortick)+(onibus*valoron))):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")