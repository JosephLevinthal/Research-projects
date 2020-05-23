w = input("Digite (L/S): ")
quant1 = int(input("Quantidade: "))
quant2 = int(input("Quantidade: "))
vl = 5.00 * quant1
s = 3.50 * quant1
r = 4.00 * quant2
if (w == "L"):
	print(round(vl+r,2))
else: 
	print(round(s+r,2))