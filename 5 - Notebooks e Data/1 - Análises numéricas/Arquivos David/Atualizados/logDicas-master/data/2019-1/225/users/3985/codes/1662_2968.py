var= input("Quant de Lanches (L/S)? ")
S= int(input("Quant de salg ou lanches: "))
R= int(input("Quant de refri: "))

if(var == "L"):
	msg= (S*5)+(R*4)
else:
	msg= (S*3.5)+(R*4)

print(round(msg, 2))