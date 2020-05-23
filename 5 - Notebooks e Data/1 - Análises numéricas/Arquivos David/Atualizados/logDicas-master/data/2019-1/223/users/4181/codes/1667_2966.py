Prog = input("S/N")
Preco = float(input("valor ing"))
quant = int(input("quantidade"))
var = quant*Preco
desc = (var - (var*20/100))
if(Prog == "S"):
	print(round(desc, 2))
else:
	print(round(var, 2))